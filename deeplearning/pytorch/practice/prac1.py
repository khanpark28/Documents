import torch
import torch.autograd, torch.nn, torch.optim, torch.utils.data, torch.onnx

print(torch.__version__)

words = ""

libraries = [torch.autograd, torch.nn, torch.optim, torch.utils.data, torch.onnx]
library_name = ['torch.autograd', 'torch.nn', 'torch.optim', 'torch.utils.data', 'torch.onnx']

for idx, library in enumerate(libraries):
    print("######################### : " + library_name[idx])
    keywords = dir(library)
    keywords.sort()
    for keyword in keywords:
        if words == "":
            words += keyword
        else:
            if keyword[0] == words[0]:
                words += keyword + " "
            else:
                print(words + "\n")
                words = keyword
