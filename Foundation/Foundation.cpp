// Copyright (C) 2005-2008 Washington University in St Louis, Baylor College of Medicine.  All rights reserved
// Author:        Sasakthi S. Abeysinghe (sasakthi@gmail.com)
// Description:   A dummy cpp file for the FOUNDATION module.

// CVS Meta Information: 
//   $Source$
//   $Revision$
//   $Date$
//   $Author$
//   $State$
//
// History Log: 
//   $Log$
//   Revision 1.9  2008/09/29 15:45:09  ssa1
//   Adding in CVS meta information
//


#define _CRT_SECURE_NO_DEPRECATE 1
#define _CRT_NONSTDC_NO_DEPRECATE 1

#ifndef FOUNDATION_SWITCHBOARD_CPP
#define FOUNDATION_SWITCHBOARD_CPP

#include "TimeManager.h"
#include "StringUtils.h"
#include "Octree.h"
#include "GraphBase.h"
#include <vector>
#include <set>


using namespace wustl_mm::Foundation;

int main( int args, char * argv[] ) {
	/*Octree<bool> * tree = new Octree<bool>(8, 8, 8);
	tree->PrintStructure();
	tree->AddNewLeaf(4, 0, 0, 1);z
	printf("\n\n");
	tree->PrintStructure();
	vector<OctreeNode<bool> *> intersects = tree->IntersectRay(Vector3DFloat(0,0,1), Vector3DFloat(5, 1, -10), 0.01);
	printf("Intersections: \n");
	for(unsigned int i = 0; i < intersects.size(); i++) {
		printf("%d %d %d - %d \n", intersects[i]->pos[0], intersects[i]->pos[1], intersects[i]->pos[2], intersects[i]->cellSize); 
	}
	return 0; */

	GraphBase<bool, bool> graph;
	vector<unsigned long long> vertices;

	for(unsigned int i = 0; i < 10; i++) {		
		vertices.push_back(graph.AddVertex(3, false));
	}
	printf("Try1 \n");
	graph.PrintAllCliques(graph.GetAllMaximalCliques());

	if(graph.IsClique(vertices)) {
		printf("clique \n");
	} else {
		printf("not clique \n");
	}

	for(unsigned int i = 0; i < 5; i++) {
		for(unsigned int j = 0; j < 5; j++) {
			graph.AddEdge(i, j, 1.0f, false);
		}
	}

	printf("Try2 \n");
	graph.PrintAllCliques(graph.GetAllMaximalCliques());

	graph.AddEdge(6, 8, 1.0f, false);
	graph.AddEdge(2, 5, 1.0f, false);
	printf("ConnComponents\n");
	graph.PrintAllCliques(graph.GetAllConnectedComponents());

	printf("Try3 \n");
	graph.PrintAllCliques(graph.GetAllMaximalCliques());

	if(graph.IsClique(vertices)) {
		printf("clique \n");
	} else {
		printf("not clique \n");
	}

	set<unsigned long long> vert;
	vert.insert(10);
	vert.insert(2);
	vert.insert(15);
	vert.insert(11);


	set<unsigned long long> vert2;
	vert2.insert(10);
	vert2.insert(2);
	vert2.insert(11);
	vert2.insert(15);
	

	if(vert == vert2) {
		printf("Same\n");
	} else {
		printf("not same\n");
	}


	TimeManager m;
	for(int i = 1; i <= 20; i++) {
		GraphBase<bool, bool> g;
		for(int j = 0; j < i; j++) {
			g.AddVertex(0, false);
		}

		m.PushCurrentTime();
		g.GetAllMaximalCliques();
		printf("%d ", i);
		m.PopAndDisplayTime(" nodes (empty graph): time = %f \n");

		for(int j = 0; j < i; j++) {
			for(int k = 0; k < i; k++) {
				g.AddEdge(j, k, 0, false);
			}
		}

		//m.PushCurrentTime();
		//g.GetAllMaximalCliques();
		//printf("%d ", i);
		//m.PopAndDisplayTime(" nodes (full graph): time = %f \n");
	}

	return 0;
}



#endif