task_list = [{'id': 1, 'name': '浏览好物', 'limit': 1, 'num1': 10, 'num2': 0, 'is_finish': False, 'finish_num': 0},
             {'id': 2, 'name': '绑定产品送抽奖机会', 'limit': 3, 'num1': 1, 'num2': 1, 'is_finish': False, 'finish_num': 0},
             {'id': 3, 'name': '邀请好友种大米', 'limit': 5, 'num1': 30, 'num2': 20, 'is_finish': False, 'finish_num': 0},
             {'id': 4, 'name': '上传菜谱', 'limit': 1, 'num1': 60, 'num2': 50, 'is_finish': False, 'finish_num': 0},
             {'id': 5, 'name': '分享菜谱', 'limit': 5, 'num1': 20, 'num2': 0, 'is_finish': False, 'finish_num': 0},
             {'id': 6, 'name': '收取他人大米', 'limit': 3, 'num1': 5, 'num2': 0, 'is_finish': True, 'finish_num': 3},
             {'id': 7, 'name': '每日问答', 'limit': 2, 'num1': 5, 'num2': 0, 'is_finish': False, 'finish_num': 0},
             {'id': 8, 'name': '其他任务', 'limit': 0, 'num1': 0, 'num2': 0, 'list': [
                 {'id': 3, 'name': '精选菜谱', 'desc': '测试*', 'rice_num': 5,
                  'url': '/pages/menuIndex/index?cl_sr=%E5%B0%8F%E7%94%B5&amp;amp;amp;amp;amp;cl_ctnm=rice',
                  'is_link': False, 'is_finish': False}]},
             {'id': 9, 'name': '活动开始、进度提醒', 'limit': 1, 'num1': 10, 'num2': 0, 'is_finish': True, 'finish_num': 0}]
#
# print(task_list[0]['id'])
# for i in len(task_list):
#     _id, name, is_finish = task_list[i]['id'], task_list[i]['name'], task_list[i]['is_finish']
for task in task_list:
    if task['id'] != 8:
        _id, name, is_finish = task['id'], task['name'], task['is_finish']
        print(_id, name, is_finish)
