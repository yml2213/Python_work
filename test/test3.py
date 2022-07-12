import random

_list = [{'id': 90316, 'nickname': '本****°',
          'avatar': 'https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKX20gJ2YDebAQjoRDFiaWS5f4mk80gcPAUydEKqXrjyJ3RFQ7LoyxYAlC6swOEQFk70ChVribhdHqQ/132',
          'rice_num': 0, 'is_visit': 0}, {'id': 176999, 'nickname': '回****',
                                          'avatar': 'https://thirdwx.qlogo.cn/mmopen/vi_32/Q3auHgzwzM5T7snVuiaMyXknyxX1gVvHJ86u8DVTrbIeo6fzphxaPhic6Fuu4xiajLlGsm6RVFEoV4ibBDV8DqFocg/132',
                                          'rice_num': 0, 'is_visit': 0}, {'id': 172070, 'nickname': '柒****',
                                                                          'avatar': 'https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLbKAyOhJxPsYQCbic9KX6gibtRzAia8va3Qw3hUbIRHABty63N0z3dnia0xicsvSBLQKVz1n5g9TmFlfA/132',
                                                                          'rice_num': 0, 'is_visit': 0},
         {'id': 41844, 'nickname': '冷****知',
          'avatar': 'https://thirdwx.qlogo.cn/mmopen/vi_32/5eN5RMSNyoyc6ACcaw6RkZEkiaszFwzASicc5iauzcfn3r6R7ISjUtj40JXTUqP6tNc6ma9uA3O5icIezW0xX8SKKw/132',
          'rice_num': 0, 'is_visit': 0}, {'id': 53168, 'nickname': '雷****',
                                          'avatar': 'https://thirdwx.qlogo.cn/mmopen/vi_32/sa5QVuNDtJp0sqRktDHicDRkrcYJUl8eU3jWqq0dhriaO8eibuLw6ibe7icVUr1nQkc5O4vVBt27vyCuCLwTBSuow4g/132',
                                          'rice_num': 0, 'is_visit': 0}, {'id': 93741, 'nickname': '王****',
                                                                          'avatar': 'https://thirdwx.qlogo.cn/mmopen/vi_32/g3fJdndGZwB2ic9vzcF6vXcX6miaIicw73OwMZibq0ibOXkwawESel8I8iaKQibbbkATAp7Ghsp1SBr49D2zyiaB6ZRibsA/132',
                                                                          'rice_num': 0, 'is_visit': 0},
         {'id': 120819, 'nickname': '袁****',
          'avatar': 'https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTIdugCgxHicXK7PYMEoquKwcgappQQbbAIBGd9KI5wOTDAy1PR5EjgTKUzGJFrfL5xX5I7rdESoPew/132',
          'rice_num': 0, 'is_visit': 0}, {'id': 101825, 'nickname': '霍****',
                                          'avatar': 'https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLwTWNr8mwibj4FfHFZYSA6pWRI3yJAibibibQo23f4UHjmKvCos62qWIhSibGpKoeHicuGlZ2WZic2MMCeA/132',
                                          'rice_num': 0, 'is_visit': 0}, {'id': 80836, 'nickname': '一****于',
                                                                          'avatar': 'https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTIknyQ7dnFK0shbrG36I8OiceBQFEk7eU8X6fefta7oFnHLKbeOsK6gJOuObYjzL3kL9kbkkdIGkWg/132',
                                                                          'rice_num': 15, 'is_visit': 0},
         {'id': 22543, 'nickname': '小****',
          'avatar': 'https://thirdwx.qlogo.cn/mmopen/vi_32/srXccQ6hKjzzKzDeVwJ7hYnh8drqP9j1cMxLrLEkFPTg1RLSNaNWpJEE4P6u3ITQoiaWU3JfM7Bnmahc6QtdNKg/132',
          'rice_num': 0, 'is_visit': 0}]

# print(_list)

random_list = random.sample(range(1, 10), 3)
print(random_list)
_id_list = []
for i in random_list:
    _id = _list[i]['id']
    _id_list.append(_id)
print(_id_list)
