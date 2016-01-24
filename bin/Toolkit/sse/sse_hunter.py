import logging
from libpycore import *
from .sse_math import *
from termcolor import colored


class pySSEHunter(object):

    def __init__(self, volume, skeleton, output):
        self.logger = logging.getLogger(__name__)
        
        self.volume = Volume()
        self.volume.loadFile(volume)
        self.logger.debug("%s before getVolume" % self.volume)
        self.logger.debug("self.volume.getSize(): %d" % self.volume.getSize())
#         self.volume = self.volume.getVolume()
        self.logger.debug("%s after getVolume" % self.volume)
        self.logger.debug("self.volume.getSize(): %d" % self.volume.getSize())
#         exit()
        
        self.skeleton = MeshRenderer()
        self.logger.debug(self.volume)
        self.logger.debug("self.volume.getSize(): %d" % self.volume.getSize())
        self.logger.debug(self.skeleton)
        self.logger.debug("after MeshRenderer(): self.skeleton.getSize(): %d" % self.skeleton.getSize())
        
        self.skeleton.loadFile(skeleton)
        self.logger.debug(self.skeleton)
        self.logger.debug(colored("after loadFile(skeleton): self.skeleton.getSize(): %d" % self.skeleton.getSize(), "yellow"))
        self.skeleton = self.skeleton.getMesh()
        self.logger.debug(self.skeleton)
        self.logger.debug(colored("after skeleton.getMesh(): self.skeleton.getSize(): %d" % self.skeleton.getSize(), "cyan"))

        self.output = output
        self.calphaRenderer = CAlphaRenderer()
        
#         SSEHunterEngine
        self.resolution = 8.0
        self.threshold = 0.38
        
        self.sseh = SSEHunter()
        
        self.run()
        self.savePseudoatoms()

    def savePseudoatoms(self):
        self.calphaRenderer.saveSSEHunterFile(self.output)
    
    def run(self):
        self.logger.debug(self.volume)
        self.logger.debug("self.volume.getSize(): %d" % self.volume.getSize())
        self.logger.debug(self.skeleton)
        self.logger.debug("self.skeleton.getSize(): %d" % self.skeleton.getSize())

        correlationWeight = 1.0
        skeletonWeight = 1.0
        geometryWeight = 1.0

        #self.calphaViewer.run( threshold, resolution, correlationWeight, skeletonWeight, geometryWeight )
        self.logger.debug(self.volume)
        self.logger.debug("self.volume.getSize(): %d" % self.volume.getSize())
        patoms = self.getScoredAtoms(correlationWeight, skeletonWeight, geometryWeight)
        
        for pseudoatom in patoms:
            self.calphaRenderer.addAtom(pseudoatom)

    def getScoredAtoms(self, correlationWeight, skeletonWeight, geometryWeight):
        self.createPseudoAtoms()
        self.setSkeletonScores()
        self.setCorrelationScores()
        numPAtoms = self.getNumberOfPseudoAtoms()
        pseudoatoms = [self.getPseudoAtom(i) for i in range(numPAtoms)]
        corrScores = [p.getCorrelationScore() for p in pseudoatoms]
        self.setGeometryScores(corrScores)
        
        origin = (self.volume.getOriginX(), self.volume.getOriginY(), self.volume.getOriginZ())
        apix = (self.volume.getSpacingX(), self.volume.getSpacingY(), self.volume.getSpacingZ())
        for i in range(len(pseudoatoms)):
            pAtom = pseudoatoms[i]
            loc = pAtom.getPosition()
            loc = [loc.x(), loc.y(), loc.z()]
            loc[0] -= origin[0] #getting them like in the ssehunter3.py printout of EMAN1
            loc[1] -= origin[1]
            loc[2] -= origin[2]
            score = correlationWeight*pAtom.getCorrelationScore()
            score += skeletonWeight*pAtom.getSkeletonScore()
            score += geometryWeight*pAtom.getGeometryScore()
            pAtom.setTempFactor(score)
            print "%3i: (%6.2f, %6.2f, %6.2f)\tCorr: %6.3f\tSkel: %6.3f\tGeom: %6.3f\tOverall: %6.3f" % (i+1, loc[0], loc[1], loc[2], pAtom.getCorrelationScore(), pAtom.getSkeletonScore(), pAtom.getGeometryScore(), score)
        return pseudoatoms
        
    def createPseudoAtoms(self):
        self.logger.debug(self.volume)
        self.logger.debug("self.volume.getSize(): %d" % self.volume.getSize())

        self.sseh.createPseudoAtoms(self.volume, self.resolution, self.threshold)
        
        self.logger.debug(self.volume)
        self.logger.debug(colored("self.volume.getSize() %d" %  self.volume.getSize(), 'magenta'))

    def getNumberOfPseudoAtoms(self):
        return self.sseh.getNumberOfPseudoAtoms()
        
    def getPseudoAtom(self, index):
        return self.sseh.getPseudoAtom(index)
        
    def setCorrelationScores(self, radialProfileType = None, deltaAngleRadians= None):
        if not radialProfileType:
            radialProfileType = RadialProfileType.polynomial
        if not deltaAngleRadians:
            deltaAngleRadians = 5*pi/180
        self.sseh.setCorrelationScores(self.volume, radialProfileType, self.resolution, deltaAngleRadians)
        
    def setSkeletonScores(self):
        self.logger.debug(colored("%s %d" % (self.volume, self.volume.getSize()), "yellow"))
        self.logger.debug(colored("%s %d" % (self.skeleton, self.skeleton.getSize()), "yellow"))
        self.sseh.setSkeletonScores(self.volume, self.skeleton, self.resolution)

    def setGeometryScores(self, correlationScores):
        #self.sseh.setGeometryScores(self.volume, self.resolution, self.threshold)
        numPAtoms = self.getNumberOfPseudoAtoms()
        pseudoatoms = [self.getPseudoAtom(i) for i in range(numPAtoms)]
        patom_coords = [(p.getPosition()) for p in pseudoatoms]
        patom_coords = [(v3d.x(), v3d.y(), v3d.z()) for v3d in patom_coords]
        patom_numbers = [p.getSerial() for p in pseudoatoms]
        
        avgCorrScore = float(sum(correlationScores)) / numPAtoms
        geometryScores = self.geometry_scores(patom_coords, patom_numbers, correlationScores, avgCorrScore)
        
        for i in range(numPAtoms):
            pAtom = pseudoatoms[i]
            pAtom.setGeometryScore(geometryScores[i])
        
#         atom_distances_matrix = self.getAtomDistances()
#
#         localDirectionalityScores = self.getLocalDirectionalityScores()
#         numPAtoms = self.getNumberOfPseudoAtoms()
#         assert len(localDirectionalityScores) == numPAtoms
#         for i in range(numPAtoms):
#             pseudoatom = self.getPseudoAtom(i)
#             score = localDirectionalityScores[i]
#             #score += ???
#             #socre += ???
#             pseudoatom.setGeometryScore(score)
        
    def getAtomDistances(self):
        return self.sseh.getAtomDistances()
        
    def getNeighborhoodVoxels(self):
        return self.sseh.getNeighborhoodVoxels(self.volume, threshold)
        
    def getLocalDirectionalityScores(self):
        return self.sseh.getLocalDirectionalityScores(self.volume)
    
    def geometry_scores(self, patoms, atomNumber, coeffArray, avghhvalue):
        '''
        psuedoatom geometry calculations -- modified from e2ssehunter.py in EMAN2
        '''
        
        atomCount=len(patoms)
        distance = self.getAtomDistances()
        pseudoatomArray=[]
        neighborhood=[]
        pointcloud=[]
        betadistance=8.25
        
        aspectRatioScores = self.getLocalDirectionalityScores()
        
        for index1 in range(atomCount):
            ### checks for nearest atoms and nearest helical atoms
            ### Identifying related pseudoatoms
            
            ################### Note by Ross #####################
            # coeffArray stores the cross-correlation based scores for the pseudoatoms
            # It seems that helixneighbor1 is the closest pseudoatom which is likely to be a helix atom based on coeffArray
            # The distance to helixneighbor1 is mindistance1
            # helixneighbor2 is the second closest and its distance is mindistance2
            # neighbor3 is the closest neighbor regardless of the cross-correlation score, and mindistance3 is the distance to it
            # neighbor4 is the second closest neighbor, and mindistance4 is the distance to it
            # Note: distances to nighbors must be at least 0.1
            #######################################################
            
            mindistance1=99998
            mindistance2=99999
            helixneighbor1=0
            helixneighbor2=0
            mindistance3=99998
            mindistance4=99999
            neighbor3=0
            neighbor4=0
            cloud=[]
            for index2 in range(atomCount):
                if distance[index1][index2]<=betadistance and index1!=index2:
                    cloud.append(atomNumber[index2])
                if distance[index1][index2] <= mindistance2 and distance[index1][index2]>0.1 and coeffArray[index2]>=avghhvalue:
                    if distance[index1][index2] <= mindistance1:
                        mindistance2=mindistance1
                        mindistance1=distance[index1][index2]
                        helixneighbor2=helixneighbor1
                        helixneighbor1=atomNumber[index2]
                    else:
                        mindistance2=distance[index1][index2]
                        helixneighbor2=atomNumber[index2]
        
                if distance[index1][index2] <= mindistance4 and distance[index1][index2]>0.1:
                    if distance[index1][index2] <= mindistance3:
                        mindistance4=mindistance3
                        mindistance3=distance[index1][index2]
                        neighbor4=neighbor3
                        neighbor3=atomNumber[index2]
                    else:
                        mindistance4=distance[index1][index2]
                        neighbor4=atomNumber[index2]
            neighbors=(helixneighbor1,helixneighbor2,mindistance1,mindistance2,neighbor3, neighbor4)
            pointcloud.append(cloud)
            neighborhood.append(neighbors)
        
        sheetlist=[]
        generallist=[]
        helixlist=[]
        
        ### Checking local gemoetry
        for index3 in range(atomCount):
        ### check generic angles
            origin=index3
            p1=neighborhood[index3][4]-1
            p2=neighborhood[index3][5]-1
            genericAngle=get_angle(patoms,origin,p1,p2)
        
        ### checks helix angles
            p1=neighborhood[index3][0]-1
            p2=neighborhood[index3][1]-1
            helixAngle=get_angle(patoms, origin, p1, p2)
    
        ###checks sheet angles
            cloud=pointcloud[index3]
            arrayofxp=[]
            for firstpoint in cloud:
                point1=firstpoint-1
                pv1=(patoms[point1][0]-patoms[origin][0],patoms[point1][1]-patoms[origin][1],patoms[point1][2]-patoms[origin][2])
                lengthPV1=sqrt(pv1[0]**2+pv1[1]**2+pv1[2]**2)
                pv1n=(pv1[0]/lengthPV1,pv1[1]/lengthPV1,pv1[2]/lengthPV1)
        
                for secondpoint in cloud:
                    point2=secondpoint-1
                    if point2 != point1 and point2 != origin:
                        pv2=(patoms[point2][0]-patoms[origin][0],patoms[point2][1]-patoms[origin][1],patoms[point2][2]-patoms[origin][2])
                        lengthPV2=sqrt(pv2[0]**2+pv2[1]**2+pv2[2]**2)
                        pv2n=(pv2[0]/lengthPV2,pv2[1]/lengthPV2,pv2[2]/lengthPV2)
                        xp=cross_product(pv1,pv2)
                        lengthxp=sqrt(xp[0]**2+xp[1]**2+xp[2]**2)
                        if lengthxp>0:
                            xpn=(xp[0]/lengthxp, xp[1]/lengthxp, xp[2]/lengthxp)
                        else:
                            xpn=(xp[0], xp[1], xp[2])
                        arrayofxp.append(xpn)
            dpxpcounter=0
            dpxpsum=0
    
            if len(arrayofxp) >=2:
                for dpxp1 in arrayofxp:
                    for dpxp2 in arrayofxp:
                        if dpxp1 != dpxp2:
                            dpxp = dpxp1[0]*dpxp2[0] + dpxp1[1]*dpxp2[1] + dpxp1[2]*dpxp2[2] #dot product
                            if dpxp > 1:
                                dpxpAngle=0
                            elif dpxp<-1:
                                dpxpAngle=180
                            else:
                                dpxpAngle=acos(dpxp)*(180/pi)
                            if dpxpAngle>90:
                                dpxpAngle=180-dpxpAngle
        
                            dpxpcounter=dpxpcounter+1
                            dpxpsum=dpxpsum+dpxpAngle
                if dpxpsum==0 and dpxpcounter==0:
                    betaAngle=0
                else:
                    betaAngle=dpxpsum/dpxpcounter
            else:
                betaAngle=90
        
            aspectRatioScore=aspectRatioScores[index3]
            #print "%d: axis: %f, neighbor angle: %f, helix angle: %f, sheet angle: %f,  number of neighbors: %d" % (atomNumber[index3], aspectRatioScore, genericAngle, helixAngle, betaAngle, len(cloud))
            pascore = aspectRatioScore
            if genericAngle <=40:
                pascore=pascore+1
            if genericAngle >=50:
                pascore=pascore-1
            if helixAngle <=45 and mindistance1<12:
                pascore=pascore+0.5
            if helixAngle <=45 and mindistance2<12:
                pascore=pascore+0.5
            if betaAngle >=30 and betaAngle !=90:
                pascore=pascore-1
            if len(cloud) <= 3:
                pascore=pascore+1
            if len(cloud) > 3:
                pascore=pascore-1
            pseudoatomArray.append(float(pascore/4.0))
    
        return pseudoatomArray
    
