/*
 * Vertex.cpp
 *
 * Author: shadow_walker <shadowwalkersb@gmail.com>
 *
 */

#include "Vertex.h"

namespace Core {

    Vertex::Vertex()
            : Vec3F(0, 0, 0)
    {}

    Vertex::Vertex(Vec3F pos)
            : Vec3F(pos)
    {}

    TKey Vertex::addFaceHash(TKey hash) {
        ids.push_back(hash);
        return hash;
    }

    unsigned int Vertex::sizeFaceHashes() const {
        return ids.size();
    }

    vector<TKey> Vertex::getFaceHashes() const {
        return ids;
    }

    TKey Vertex::edge(int i) const {
        return ids[i];
    }

    TKey Vertex::sizeEdge() const {
        return sizeFaceHashes();
    }

    ostream& operator<<(ostream& out, const Vertex& obj) {
        return out//<<"\033[34m"
                <<Vec3F(obj)
                <<"\tedgeIds.size(): "<<obj.sizeFaceHashes()
                <<endl<<obj.getFaceHashes()
                <<endl;
//                      <<"\033[0m";
    }

}

