import get_trace
import numpy as np

cnfs = get_trace.cnfs


def get_score(prop, watcher, clause):
    """

    :return: float
    :type prop:float
    :type watcher: float
    :type clause: float

    """
    return 0.15 * prop + 0.15 * watcher + 0.7 * clause


if __name__ == "__main__":

    for cnf in cnfs:
        print(cnf)
        f = "."

        prop = np.load("{}/{}/prop.out.bin.npy".format(f, cnf))
        watcher = np.load("{}/{}/watcher.out.bin.npy".format(f, cnf))
        clause = np.load("{}/{}/clause.out.bin.npy".format(f, cnf))
        prop = prop / np.max(prop)
        watcher = watcher / np.max(watcher)
        clause = clause / np.max(clause)

        average_prop = np.average(prop)
        average_watcher = np.average(watcher)
        average_clause = np.average(clause)

        target_score = 0.15 * average_prop + 0.15 * average_watcher + 0.7 * average_clause

        first_prop_200 = np.sum(prop[0:200])
        first_watcher_200 = np.sum(watcher[0:200])
        first_clause_200 = np.sum(clause[0:200])

        size = len(prop)
        print(f"size {size}")
        prop_200_array = np.zeros_like(prop)
        watcher_200_array = np.zeros_like(watcher)
        clause_200_array = np.zeros_like(clause)
        last_score=0
        find=False
        for i in range(size - 200):
            prop_200_array[i] = first_prop_200 / 200
            first_prop_200 -= prop[i]
            first_prop_200 += prop[i + 200]

            watcher_200_array[i] = first_watcher_200 / 200
            first_watcher_200 -= watcher[i]
            first_watcher_200 += watcher[i + 200]

            clause_200_array[i] = first_clause_200 / 200
            first_clause_200 -= clause[i]
            first_clause_200 += clause[i + 200]

            current_score=get_score(prop_200_array[i],watcher_200_array[i],clause_200_array[i])
            if(last_score<=target_score and current_score>=target_score):
                #next 200 record can be the represent gap
                find=True
                print(i)
                break
        if not find:
            print(f"error:{get_score(prop_200_array[size-200-1],watcher_200_array[size-200-1],clause_200_array[size-200-1])} {target_score}")
