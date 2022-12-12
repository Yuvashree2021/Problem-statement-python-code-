import csv
import sys
class Restaurant:

    # Read CSV file and convert to Dictionary
    def readcsv(self, filepath):
        myFile = open(filepath, 'r')
        reader = csv.DictReader(myFile)
        myList = list(reader)
        return myList


    # Check for Duplicates
    def checkduplicates(self, list):
        eat = []
        food = []
        for x in list:
            # print(x['eater_id'],x['foodmenu_id'])
            if ((x['eater_id'] in eat) and (x['foodmenu_id'] in food)):
                print('------------------------------------------------')
                print("Error: This eater id:" + x['eater_id'] + ' has same food menu id:' + x['foodmenu_id'])
                print('------------------------------------------------')
                food.clear()
                return food
            else:
                eat.append(x['eater_id'])
                food.append(x['foodmenu_id'])

        return food

    # Main Code Logic
    def topthree(self, path1, path2):
        import csv
        restaurant = Restaurant();
        # eaterList = restaurant.readcsv("P:\\Barracuda_BKP\\Python\\data\\eaterlog.csv")
        # foodList = restaurant.readcsv("P:\\Barracuda_BKP\\Python\\data\\foodmenu.csv")
        eaterList = restaurant.readcsv(path1)
        foodList = restaurant.readcsv(path2)
        foodid = restaurant.checkduplicates(eaterList)
        items = []
        if len(foodid) != 0:
            for x in foodid:
                for y in foodList:
                    if y['foodmenu_id'] == x:
                        items.append(y['fooditems'])

            counts = dict()
            for i in items:
                counts[i] = counts.get(i, 0) + 1

            sortedDict = sorted(counts.items(), key=lambda x: x[1], reverse=True)

            topitems = []
            for i in range(3):
                topitems.append(sortedDict[i][0])
            print('------------------------------------------------')
            print('Top 3 Food Items Consumed:', *topitems, sep="\n")
            print('------------------------------------------------')


if __name__ == '__main__':
     restaurant = Restaurant();
     restaurant.topthree(sys.argv[1], sys.argv[2])
