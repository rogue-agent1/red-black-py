#!/usr/bin/env python3
"""Red-black tree with insert and search."""
import sys
RED,BLACK=True,False
class Node:
    def __init__(self,key,color=RED):self.key=key;self.color=color;self.left=self.right=self.parent=None
class RBTree:
    def __init__(self):self.NIL=Node(None,BLACK);self.root=self.NIL
    def insert(self,key):
        n=Node(key);n.left=n.right=n.parent=self.NIL
        p=self.NIL;c=self.root
        while c!=self.NIL:
            p=c;c=c.left if key<c.key else c.right
        n.parent=p
        if p==self.NIL:self.root=n
        elif key<p.key:p.left=n
        else:p.right=n
        self._fix_insert(n)
    def _fix_insert(self,n):
        while n.parent.color==RED:
            if n.parent==n.parent.parent.left:
                u=n.parent.parent.right
                if u.color==RED:
                    n.parent.color=BLACK;u.color=BLACK;n.parent.parent.color=RED;n=n.parent.parent
                else:
                    if n==n.parent.right:n=n.parent;self._left_rotate(n)
                    n.parent.color=BLACK;n.parent.parent.color=RED;self._right_rotate(n.parent.parent)
            else:
                u=n.parent.parent.left
                if u.color==RED:
                    n.parent.color=BLACK;u.color=BLACK;n.parent.parent.color=RED;n=n.parent.parent
                else:
                    if n==n.parent.left:n=n.parent;self._right_rotate(n)
                    n.parent.color=BLACK;n.parent.parent.color=RED;self._left_rotate(n.parent.parent)
        self.root.color=BLACK
    def _left_rotate(self,x):
        y=x.right;x.right=y.left
        if y.left!=self.NIL:y.left.parent=x
        y.parent=x.parent
        if x.parent==self.NIL:self.root=y
        elif x==x.parent.left:x.parent.left=y
        else:x.parent.right=y
        y.left=x;x.parent=y
    def _right_rotate(self,y):
        x=y.left;y.left=x.right
        if x.right!=self.NIL:x.right.parent=y
        x.parent=y.parent
        if y.parent==self.NIL:self.root=x
        elif y==y.parent.right:y.parent.right=x
        else:y.parent.left=x
        x.right=y;y.parent=x
    def search(self,key):
        n=self.root
        while n!=self.NIL:
            if key==n.key:return True
            n=n.left if key<n.key else n.right
        return False
    def inorder(self):
        r=[];self._inorder(self.root,r);return r
    def _inorder(self,n,r):
        if n!=self.NIL:self._inorder(n.left,r);r.append(n.key);self._inorder(n.right,r)
    def _black_height(self,n):
        if n==self.NIL:return 1
        lh=self._black_height(n.left);rh=self._black_height(n.right)
        if lh!=rh:return-1
        return lh+(0 if n.color==RED else 1)
    def is_valid(self):return self._black_height(self.root)>0 and self.root.color==BLACK
def main():
    if len(sys.argv)>1 and sys.argv[1]=="--test":
        t=RBTree()
        for x in[7,3,18,10,22,8,11,26]:t.insert(x)
        assert t.inorder()==sorted([7,3,18,10,22,8,11,26])
        assert t.search(10) and not t.search(99)
        assert t.is_valid()
        t2=RBTree()
        for i in range(100):t2.insert(i)
        assert t2.is_valid() and t2.inorder()==list(range(100))
        print("All tests passed!")
    else:
        t=RBTree();[t.insert(x) for x in[5,3,8,1,4]];print(t.inorder())
if __name__=="__main__":main()
