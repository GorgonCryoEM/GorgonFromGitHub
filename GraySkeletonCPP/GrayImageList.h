// Copyright (C) 2005-2008 Washington University in St Louis, Baylor College of Medicine.  All rights reserved
// Author:        Sasakthi S. Abeysinghe (sasakthi@gmail.com)
// Description:   A storage class for a list of images

// CVS Meta Information: 
//   $Source: /project/mm/cvs/graphics/ssa1/source/GraySkeletonCPP/GrayImageList.h,v $
//   $Revision: 1.7 $
//   $Date: 2008/09/29 16:30:15 $
//   $Author: ssa1 $
//   $State: Exp $
//
// History Log: 
//   $Log: GrayImageList.h,v $
//   Revision 1.7  2008/09/29 16:30:15  ssa1
//   Adding in CVS meta information
//

#ifndef GRAYSKELETONCPP_GRAY_IMAGE_LIST_H
#define GRAYSKELETONCPP_GRAY_IMAGE_LIST_H

#include <vector>
#include "GrayImage.h"

using namespace std;

namespace wustl_mm {
	namespace GraySkeletonCPP {
		class GrayImageList {
		public:
			GrayImageList();
			void AddImage(GrayImage * image);
			void Clear(bool deleteChildObjects);
			GrayImage * GetCompositeImage(int xCount);
		private:
			vector <GrayImage *> imageList;
		};

		GrayImageList::GrayImageList() {
			imageList.clear();
		}

		void GrayImageList::AddImage(GrayImage * image) {
			imageList.push_back(image);
		}

		void GrayImageList::Clear(bool deleteChildObjects) {
			if(deleteChildObjects) {
				for(int i = imageList.size() - 1; i >=0; i--) {
					delete imageList[i];
				}
			}
			imageList.clear();
		}

		GrayImage * GrayImageList::GetCompositeImage(int xCount) {
			int imageSizeX = imageList[0]->GetSizeX();
			int imageSizeY = imageList[0]->GetSizeY();
			int yCount = (int)ceil((double)imageList.size() / (double)xCount);		
			int xImage, yImage;			
			GrayImage * compositeImage = new GrayImage(imageSizeX * xCount, imageSizeY * yCount);
			GrayImage * currentImage;

		

			
			for(unsigned int i = 0; i < imageList.size(); i++) {
				xImage = i % xCount;
				yImage = yCount - 1 - i / xCount;
				currentImage = imageList[i];
				for (int x = 0; x < imageSizeX; x++) {
					for (int y = 0; y < imageSizeY; y++) {
						compositeImage->SetDataAt(xImage * imageSizeX + x, yImage * imageSizeY + y, currentImage->GetDataAt(x, y));
					}
				}			
			}
			return compositeImage;
		}
	}
};

#endif
