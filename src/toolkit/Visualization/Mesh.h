/*
 * Mesh.h
 *
 * Author: shadow_walker <shadowwalkersb@gmail.com>
 *
 */

#ifndef SRC_TOOLKIT_VISUALIZATION_MESH_H_
#define SRC_TOOLKIT_VISUALIZATION_MESH_H_

#include <map>
#include <set>
#include <vector>
//#include <string>
//#include "OpenGLUtils.h"
#include "MathTools/Vector3.h"
#include "Vertex.h"
#include "Core/IdList.h"

using namespace std;
//using namespace Foundation;
using namespace GraphMatch;

namespace Core {

    typedef vector<IdList >   TF;
    typedef Vector3<TKey> Vec3U;

    class Mesh {
        public:
            Mesh();
            virtual ~Mesh();

            virtual int addMarchingVertex(Vec3F loc, int id);
            int addFace(IdList face);
            virtual TKey addFace(Vec3U face);

            void clear();
            TKey addVertex(Vec3F vertex, TKey id);
            Vec3F getVertexNormal(TKey id);
            Vec3F getFaceNormal(TKey faceHash);
            void draw(bool drawSurfaces, bool annotateSurfaces,
                      bool fadeExtreme, int radius, Vec3F center);

            void save(string fileName);

        private:
            typedef map<TKey, Vertex> MUV;

            MUV vertices;
            TF faces;

            friend ostream & operator<<(ostream & out, const Mesh & obj) {
                return out
                        <<"Mesh:\n"
                        <<"vertices.size(): "<<obj.vertices.size()<<endl
                        <<"faces.size(): "<<obj.faces.size()
                        <<endl;
            }

    };

} /* namespace Core */

#endif /* SRC_TOOLKIT_VISUALIZATION_MESH_H_ */
