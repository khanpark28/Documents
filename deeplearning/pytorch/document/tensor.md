0d: scalar
1d: vector
2d: matrix
3d: tensor
4d: vector of tensor
5d: matrix of tensor
....

# 2d tensor
|t| = (batch size, dimension)
- Let the size of one training data's is 215 (for example, [5,2,15,433,12, ..... ], and size is 215)
- And the number of training data is 3,000. 
- Then total training data size is 3,000 x 256
- It is a 2d tensor. 

- Whole data (3,000) could be handle one by one.
- Also could be handled by 64, and it is called as batch size
- Then 2d tensor could be handled 64 x 256 (batch size x dim)

# 3d tensor (typical computer vision)
|t| = (batch size, width, height)
- for vision data which have widht and height. 

# 3d tensor (typical natural language)
|t| = (batch, length, dim)
- for processing natural language, batch size, length of sentence and vector for word are used.
- For example, 
  1) I like an apple
  2) I like a banana
  3) I hate an apple

-> I = [0.1, 0.2, 0.9]
-> like = [0.7, 0.6, 0.5]
-> apple = [0.3, 0.5, 0.2]
-> banana = [0.1, 0.5, 0.8]
-> hate = [0.5, 0.6, 0.7]

=> [
	[[0.1, 0.2, 0.9], [0.7, 0.6, 0.5], ...],
	[[0.1, 0.2, 0.9], [0.5, 0.6, 0.7], ...]
	...
	...
   ]


