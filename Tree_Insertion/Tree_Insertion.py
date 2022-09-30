#/usr/bin/env python3

'''
Created 9/24/2019
@author Ben Mason, Trevor Little, Fin Carter
A solution for kattis problem Tree Insertion
https://open.kattis.com/problems/insert
'''

import sys

class TreeNode(object):
	"""a BST node"""
	def __init__(self, data):
		self.data = data
		self.l = None
		self.r = None
		self.children = 1

def insert(root, dta):
	# Base case
	if root == None:
		this = TreeNode(dta)
		return this
	# Branching case
	if dta < root.data:
		root.l = insert(root.l, dta)
	if dta >= root.data:
		root.r = insert(root.r, dta)
	# General case (not a leaf)
	root.children += 1
	return root

def pascalsTriangle(max = 101):
	# Build blank table
	# This max matches the domain of our problem.
	table = [[1 for i in range(max)] for j in range(max)]

	# Populate table with goodness
	for i in range(1,max):
		for j in range(1,max):
			table[i][j] = table[i-1][j] + table[i][j-1];

	return table

pTable = pascalsTriangle();
def permCount(tree):
	# Base case (tiny tree)
	if tree == None:
		return 1

	total = 1
	if (tree.l != None) and (tree.r != None):
		total = pTable[tree.l.children][tree.r.children]

	# Branching
	total *= permCount(tree.l)
	total *= permCount(tree.r)
	# General
	return total

def printTree(t):
	# Preorder traversal (CLR)
	if t is None:
		return
	print(t.data, end = ' ')
	printTree(t.l)
	printTree(t.r)

def main():
	lc = 0

	for line in sys.stdin:
		if (lc % 2 == 1):
			root = None
			intList = [int(c) for c in line.split()]
			for i in intList:
				root = insert(root,int(i))
			# printTree(root)
			print(permCount(root))

		lc += 1

if __name__ == "__main__":
    main()