drop = [5,1,2,3,4]
models = [1,2,3,4,5,6,7,8,9]
counter=0
print_prec_iou =0
with open("C:/Users/ADostovalova/Downloads/stat_file3.txt","r") as file:
    for line in file:
        if "overall Recall" in line:

            if float(line.split(":")[1]) > 0.912:
                print_prec_iou = 2
                print("drop ", str(drop[counter//len(models)]), "models ", str(models[counter%len(models)]), line)
            counter+=1
        else:
            if print_prec_iou >0:
                print(line)
                print_prec_iou -= 1
