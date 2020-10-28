# string = "banana"
# substring = "an"
# def remove_substring(substring,string):
#     n_str = ""
#     for s in range(len(string)):
#         if string[s:s+len(substring)] == substring:
#             n_str = string[0:s] + string[s+len(substring):]
#     return n_str, substring
# print (remove_substring(substring,string))


# text = "banana"
# sub = "an"
# def count_substring(substring,string):
#     new_text =''
#     i=0
#     last_i = 0
#     while i <  len(text):
#         if text[i:i+len(sub)] == sub:
#             new_text += text[last_i:i]
#             last_i=i+len(sub)
#             i=i+len(sub)
#         else:
#             i += 1
#     new_text += text[last_i:i]
#     return new_text
#
# print (count_substring(sub,text))


for(i in 1:130) {
    for(j in 1:30) {
        result <- latitude3[i,] - latitude3[j,]
        print(result)
    }
}
for(i in 1:130) {
  for(j in 1:130) {
    result <- latitude3[i,] - latitude3[j,]
    list[[i,j]] <- longdiff, latdiff
  }
}
