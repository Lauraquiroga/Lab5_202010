import unittest 
import config 
from DataStructures import rbtnode as node
from DataStructures import listiterator as it
from ADT import list as lt
from ADT import orderedmap as omap

class RBTreeTest (unittest.TestCase):


    def setUp (self):
        pass



    def tearDown (self):
        pass


    

    def comparekeys (self, key1, key2):
        if ( key1 == key2):
            return 0
        elif ( key1 < key2):
            return -1
        else:
            return 1


    def test_DisorderedRBT (self):
        """
        """
        tree = omap.newMap ()
      
        tree = omap.put (tree, 'S', 'Title 50', self.comparekeys)
        tree = omap.put (tree, 'E', 'Title 70', self.comparekeys)
        tree = omap.put (tree, 'A', 'Title 30', self.comparekeys)
        tree = omap.put (tree, 'R', 'Title 80', self.comparekeys)        
        tree = omap.put (tree, 'C', 'Title 80', self.comparekeys)
        tree = omap.put (tree, 'H', 'Title 30', self.comparekeys)
        tree = omap.put (tree, 'X', 'Title 30', self.comparekeys)
        tree = omap.put (tree, 'M', 'Title 80', self.comparekeys)
        tree = omap.put (tree, 'P', 'Title 30', self.comparekeys)
        tree = omap.put (tree, 'L', 'Title 30', self.comparekeys)
        print("\nRBT datos aleatorios")
        self.assertEqual(omap.size(tree),10)
    


if __name__ == "__main__":
    unittest.main()
