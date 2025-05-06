try:

    with open("Mars_Base_Inventory_List.csv", "rt", encoding="utf-8") as f:
        lines = f.readlines()

        for line in lines:
           print(line, end='')

        log_list = []
        for line in lines[1:]:
            parts = line.strip().split(",", 4)
            if len(parts) == 5:
                Substance = parts[0].strip()
                Weight = parts[1].strip()
                Specific_Gravity = parts[2].strip()
                Strength = parts[3].strip()
            
                try:
                    Flammability = float(parts[4].strip())
                    log_list.append((Substance,Weight,Specific_Gravity,Strength,Flammability))
                except ValueError:
                    print("값 오류")

        header = lines[0].strip().split(",")
        
        log_list.sort(key=lambda x: x[4], reverse=True)

        danger_list = [log for log in log_list if log[4] >= 0.7]
        for log in danger_list:
            print(log)

        with open("Mars_Base_Inventory_Danger_list.csv", "wt", encoding="utf-8") as f:
            f.write(",".join(header) + "\n")
            for log in danger_list:
                f.write(",".join(map(str, log)) + "\n")
 
except Exception as e:
    print("예외처리")
except FileNotFoundError as e:
    print("파일을 찾을 수 없음 ")
except IOError as e: 
    print("입출력 오류 발생")




