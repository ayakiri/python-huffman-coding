import huff as h


code_lorem = h.huffman(file="to_compress/lorem.txt")
code_lorem.compress_file(result_file_name="results/lorem_result.bin")

code_hobbit = h.huffman(file="to_compress/hobbit.txt")
code_hobbit.compress_file(result_file_name="results/hobbit_result.bin")
