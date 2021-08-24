  
############## SDT Cards Functionality ###############
#
# Author: Dayu Liu
# Date: 8/12/21
# Description: Initialize and maintain the cards pool
#

class Cards:
    def __init__(self):
        self.cardData = [ 
            ["val1", 0],
            ["asd1", 0],
            ["bbb1", 0],
            ["ccc1", 0],
            ["ddd1", 0],
            ["eee1", 0] 
        ]

    # reset cards pool
    def reloadCardPool(self):
        self.cardData = [ 
                ["val1", 0],
                ["asd1", 0],
                ["bbb1", 0],
                ["ccc1", 0],
                ["ddd1", 0],
                ["eee1", 0] 
            ]
