

def zeichne_quadrat(laenge):
    print("-" * laenge)
    s = '|' +' ' * (laenge - 2) + '|'
    for x in range(laenge - 2):
        print(s)
    print("-" * laenge)



zeichne_quadrat(10)

"""
++++++++++
+        +
+        +
+        +
+        +
+        +
+        +
+        +
+        +
+        +
++++++++++

#
##
# #
#  #
#####

"""