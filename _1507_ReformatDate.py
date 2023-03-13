class Solution:
    def reformatDate(self, date: str) -> str:
        monthDict = {"Jan" : '01', "Feb": '02', "Mar": '03', "Apr": '04', "May": '05', "Jun": '06', "Jul": '07', "Aug": '08', "Sep": '09', "Oct": '10', "Nov": '11', "Dec": '12'}
        dateList = date.split(' ')
        day = '0' + dateList[0][:-2] if int(dateList[0][:-2]) < 10 else dateList[0][:-2]
        #day = dateList[0].replace("th","").replace("nd","").replace("st","").replace("rd","")
        month = monthDict[dateList[1]]
        year = dateList[2]
        result = year + '-' + month + '-' + day
        return result