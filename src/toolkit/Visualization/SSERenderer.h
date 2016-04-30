/*
 * SSERenderer.h
 *
 * Author: shadow_walker <shadowwalkersb@gmail.com>
 *
 */

#ifndef SRC_TOOLKIT_VISUALIZATION_SSERENDERER_H_
#define SRC_TOOLKIT_VISUALIZATION_SSERENDERER_H_

#include "Display.h"

//#include "Renderer.h"
//#include "MeshRenderer.h"
//#include <ProteinMorph/SheetGenerator.h>
//#include <GraphMatch/StandardGraph.h>
//#include <GraphMatch/SkeletonReader.h>
#include <GraphMatch/Shape.h>
//#include <GraphMatch/VectorMath.h>
//#include <MathTools/LinearSolver.h>
//#include <ProteinMorph/SSEFlexibleFitter.h>
//#include <ProteinMorph/SSECorrespondenceNode.h>
//#include <vector>
//#include <map>
//#include <boost/tuple/tuple.hpp>

//using namespace Protein_Morph;
//using namespace GraySkeletonCPP;
//using namespace GraphMatch;
//using namespace MathTools;
//using namespace SkeletonMaker;
//using namespace std;
//using namespace boost::tuples;

namespace Visualization {

    const float HELIX_LENGTH_TO_RESIDUE_RATIO = 1.54;

    class SSERenderer : public Display {
        public:
            SSERenderer();
            virtual ~SSERenderer();

            vector<Shape*> * GetHelices();

            void AddHelix(Vector3DFloat p1, Vector3DFloat p2);
            void StartNewSSE();
            void AddSSEPoint(Vector3DFloat p);
            void FinalizeSheet();
            void FinalizeHelix();
            void Draw(int subSceneIndex, bool selectEnabled);
            void LoadHelixFile(string fileName);
            void LoadSheetFile(string fileName);
            void Unload();
            void LoadGraphSSE(int index, Shape* sse, float offsetx, float offsety, float offsetz, float scalex, float scaley, float scalez);
            void UnloadGraphSSEs();
            void SetHelixColor(int index, float r, float g, float b, float a);
            void SetSheetColor(int index, float r, float g, float b, float a);
            void SetSSEColor(int index, float r, float g, float b, float a);
            void SetSSEOrientationFlips(vector<bool>);
            bool SelectionRotate(Vector3DFloat centerOfMass, Vector3DFloat rotationAxis, float angle);
            int SelectionObjectCount();
            Vector3DFloat SelectionCenterOfMass();
            bool SelectionMove(Vector3DFloat moveDirection);
            bool SelectionClear();
            void SelectionToggle(int subsceneIndex, bool forceTrue, int ix0, int ix1 = -1, int ix2 = -1, int ix3 = -1, int ix4 = -1);
            void SaveHelixFile(string fileName);
            void SaveSheetFile(string fileName);
            string GetSupportedHelixLoadFileFormats();
            string GetSupportedHelixSaveFileFormats();
            string GetSupportedSheetLoadFileFormats();
            string GetSupportedSheetSaveFileFormats();
            Vector3DFloat Get3DCoordinates(int subsceneIndex, int ix0, int ix1 = -1, int ix2 = -1, int ix3 = -1, int ix4 = -1);
            void FitSelectedSSEs(Volume * vol);
            void RemoveHelices();
            void RemoveSheets();
            void RemoveSelectedSSEs();
            int GetHelixCount();
            Vector3DFloat GetHelixCorner(int helixIx, int cornerIx);
            void UpdateBoundingBox();

            vector<int> GetSelectedHelixIndices();
            void SetHelixCorrs(  vector < int > flatCorrespondences);
            void SetSelectedPDBHelices(vector<int> indices);
            void ClearOtherHighlights();
        private:
            void SheetListToMesh(vector<Shape*> & sheets);
            void LoadHelixFileSSE(string fileName);
            void LoadHelixFileVRML(string fileName);
            void SaveHelixFileSSE(FILE* fout);
            void SaveHelixFileVRML(FILE* fout);
            void SaveSheetFileVRML(FILE* fout);
            vector<Shape*> helices;
            vector<Shape*> sheets;
            NonManifoldMesh_SheetIds * sheetMesh;
            NonManifoldMesh_SheetIds * graphSheetMesh;
            int sheetCount;
            int graphSheetCount;
            bool selectedSheets[256];
            bool selectedGraphSheets[256];
            vector<Vector3DFloat> tempSSEPoints;

            vector<bool> helixFlips;
            vector<int> selectedHelices;
            vector < boost::tuple<int,int> > corrs;
            vector<int> selectedPDBHelices;
    };

} /* namespace Visualization */

#endif /* SRC_TOOLKIT_VISUALIZATION_SSERENDERER_H_ */
