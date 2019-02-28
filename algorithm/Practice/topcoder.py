# class ColorfulTilesEasy(object):
# #     def theMin(self,room):
# #         #write here
# #         room_len = len(room)
# #         tmp = list(room)
# #         flag = 0
# #         for i in range(room_len):
# #             if i > 0:
# #                 if tmp[i] == tmp[i-1]:
# #                     flag += 1
# #                     tmp[i] = '#'
# #         return flag



# class GetAccepted(object):
#     def answer(self,question):
#         question = question.split()
#         num = question.count('not')
#         if num%2 == 0:
#             return 'True.'
#         return 'False.'

        # return res


class LongJumpCompetition(object):
    def recoverStandings(self, jumpLengths):
        jumpLengths = list(jumpLengths)
        allres = len(jumpLengths)
        N = int(allres / 3)
        points = jumpLengths[0:N]
        # N : 2N
        for i in range(2):
            tmp = jumpLengths[(i+1)*N:(i+2)*N]

