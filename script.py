# def bubble_sort(data):
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(data)-1):
#             if data[i] > data[i+1]:
#                 data[i], data[i+1] = data[i+1], data[i]
#                 swapped = True
    
# if __name__ == '__main__':
#     data = [9, 5, 13, 62, 20, 190, 77, 924, 104, 2304]
#     bubble_sort(data)
#     print(data)

# for x in range(1, 101):
#     i = ''
#     if x % 3 == 0:
#         i = 'fizz'
#     if x % 5 == 0:
#         i += 'buzz'
#     print(x if not i else i)
