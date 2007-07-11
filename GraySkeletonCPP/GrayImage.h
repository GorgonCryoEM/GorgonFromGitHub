#ifndef GRAY_IMAGE_H
#define GRAY_IMAGE_H

#include "..\SkeletonMaker\reader.h"
#include "..\SkeletonMaker\volume.h"
#include "GlobalDefinitions.h"

namespace WUSTL_MM {
	const int GRAYIMAGE_IN_VOLUME_Z = 2;
	const int GRAYIMAGE_VOLUME_Z_SIZE = 5;

	class GrayImage {
	public:
		GrayImage();
		GrayImage(int sizeX, int sizeY);
		GrayImage(GrayImage * sourceImage);
		~GrayImage();

		unsigned char GetDataAt(int x, int y);
		int GetSizeX();
		int GetSizeY();
		void SetDataAt(int x, int y, unsigned char value);
		Volume * ToVolume();
		static GrayImage * GrayImageVolumeToImage(Volume * volume);
		void PrintValues();
		void Threshold(unsigned char threshold, bool preserveHighValues);
		void ApplyMask(GrayImage * maskImage, unsigned char maskValue, bool keepMaskValue);
		void Blur();
	private:
		int sizeX;
		int sizeY;
		unsigned char * data;
	};

	GrayImage::GrayImage() {
		data = NULL;
		sizeX = 0;
		sizeY = 0;
	}

	GrayImage::GrayImage(int sizeX, int sizeY) {
		this->sizeX = sizeX;
		this->sizeY = sizeY;
		data = new unsigned char[sizeX * sizeY];
		for(int x = 0; x < sizeX; x++){
			for(int y = 0; y < sizeY; y++) {
				SetDataAt(x, y, 0);
			}
		}
	}

	GrayImage::GrayImage(GrayImage * sourceImage) {
		this->sizeX = sourceImage->GetSizeX();
		this->sizeY = sourceImage->GetSizeY();
		data = new unsigned char[sizeX * sizeY];
		for(int x = 0; x < sizeX; x++){
			for(int y = 0; y < sizeY; y++) {
				SetDataAt(x, y, sourceImage->GetDataAt(x, y));
			}
		}

	}

	GrayImage::~GrayImage() {
		if(data != NULL) {
			delete [] data;
		}
	}

	unsigned char GrayImage::GetDataAt(int x, int y) {
		return data[x + sizeX * y]; 
	}

	int GrayImage::GetSizeX() {
		return sizeX;
	}

	int GrayImage::GetSizeY() {
		return sizeY;
	}

	void GrayImage::SetDataAt(int x, int y, unsigned char value) {
		data[x + sizeX * y] = value;
	}

	Volume * GrayImage::ToVolume() {
		Volume * vol = new Volume(sizeX, sizeY, 5);
		for(int z = 0; z < GRAYIMAGE_VOLUME_Z_SIZE; z++) {
			for(int x = 0; x < sizeX; x++) {
				for(int y = 0; y < sizeY; y++) {		
					if(z == GRAYIMAGE_IN_VOLUME_Z) {
						vol->setDataAt(x, y, z, (double)GetDataAt(x, y));
					}
					else {
						vol->setDataAt(x, y, z, 0);
					}
				}
			}
		}
		return vol;
	}
	GrayImage * GrayImage::GrayImageVolumeToImage(Volume * volume) {
		GrayImage * image = new GrayImage(volume->getSizeX(), volume->getSizeY());
		double minValue = volume->getDataAt(0,0,5);
		double maxValue = volume->getDataAt(0,0,0);
		double currValue;

		for(int x = 0; x < volume->getSizeX(); x++) {
			for(int y = 0; y < volume->getSizeY(); y++) {
				currValue = volume->getDataAt(x, y, GRAYIMAGE_IN_VOLUME_Z);
				if(currValue < minValue) {
					minValue = currValue;
				}
				if(currValue > maxValue) {
					maxValue = currValue;
				}
			}
		}
		if(minValue == maxValue) {
			for(int x = 0; x < volume->getSizeX(); x++) {
				for(int y = 0; y < volume->getSizeY(); y++) {
					image->SetDataAt(x, y, 0);
				}
			}
		}

		for(int x = 0; x < volume->getSizeX(); x++) {
			for(int y = 0; y < volume->getSizeY(); y++) {
				image->SetDataAt(x, y, (unsigned char)((volume->getDataAt(x, y, GRAYIMAGE_IN_VOLUME_Z) - minValue) * 255.0 / (maxValue - minValue)));
			}
		}
		return image;
	}
	void GrayImage::PrintValues() {
		for(int y = 0; y < sizeY; y++) {
			for(int x = 0; x < sizeX; x++) {
				printf("%i, ", GetDataAt(x, y));
			}
			printf("\n");
		}
	}
	void GrayImage::Threshold(unsigned char threshold, bool preserveHighValues) {
		for(int x = 0; x < sizeX; x++) {
			for(int y = 0; y < sizeY; y++) {
				if(GetDataAt(x, y) < threshold) {
					SetDataAt(x, y, PIXEL_BINARY_FALSE);
				} else if (!preserveHighValues) {
					SetDataAt(x, y, PIXEL_BINARY_TRUE);
				}
				
			}
		}
	}
	void GrayImage::ApplyMask(GrayImage * maskImage, unsigned char maskValue, bool keepMaskValue) {
		for(int x = 0; x < maskImage->GetSizeX(); x++) {
			for(int y = 0; y < maskImage->GetSizeY(); y++) {
				if(((maskImage->GetDataAt(x, y) == maskValue) && !keepMaskValue) ||
					((maskImage->GetDataAt(x, y) != maskValue) && keepMaskValue)) {
					SetDataAt(x, y, 0);
				}
			}
		}
	}
	void GrayImage::Blur() {
		GrayImage * tempImage = new GrayImage(this);
		int total;
		for(int x = 1; x < sizeX-1; x++) {
			for(int y = 1; y < sizeY-1; y++) {
				total = 0;
				for(int xx = -1; xx <= 1; xx++) {
					for(int yy = -1; yy <= 1; yy++) {
						total += (int)GetDataAt(x+xx, y+yy);
					}
				}
				tempImage->SetDataAt(x, y, (unsigned char)((double)total/9.0));
			}
		}

		for(int x = 1; x < sizeX-1; x++) {
			for(int y = 1; y < sizeY-1; y++) {
				SetDataAt(x, y, tempImage->GetDataAt(x, y));
			}
		}
		delete tempImage;
	}
};


#endif 