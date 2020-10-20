import numpy as np
import matplotlib.pyplot as plt

def editing_file (filename):
    data = np.loadtxt(filename)
    year, hares, lynxes, carrots = data.T  # trick: columns to variables
    ma = int(max(year))
    mi = int(min(year))
    x_years = np.linspace(mi, ma, 5)
    """
    Questions
    """
    # Which year each species had the largest population?
    hares_max = np.argmax(hares)
    hares_max = year[hares_max] # print this for result
    lynxes_max = np.argmax(lynxes)
    lynxes_max = year[lynxes_max] # print this for result
    carrots_max = np.argmax(carrots)
    carrots_max = year[carrots_max] # print this for result

    # Which species has the largest population for each year?
    populations = data[:, 1:]
    max_species = np.argmax(populations, axis=1) # axis = 0 -> counts for each column; axis = 1 ->  count foe each row
    species = np.array(['Hare', 'Lynx', 'Carrot']) # taking the headers
    # print("Max species:")
    # print(year)
    # print(species[max_species])

    #Print in terminal: Which years any of the populations is above 50, 000
    above_50000 = np.any(populations > 50000, axis=1)
    # print("Any above 50000:", year[above_50000])

    # """
    # plot 1
    # """
    # plt.plot(year, hares, color = "blue")
    # plt.plot(year, lynxes, color = "red")
    # plt.plot(year, carrots, color = "green")
    # plt.title("populations of hares, lynxes and carrots")
    # plt.ylabel("Amount")
    # plt.xlabel("years")
    # plt.xticks(x_years)
    # plt.legend(('Hare', 'Lynx', 'Carrot'))
    # plt.show ()

    """
    plot 2
    """
    # hare_dying = np.gradient(hares, -1)
    # plt.title("relation between lynx population and the hare death rate")
    # plt.ylabel("Amount")
    # plt.xlabel("years")
    # plt.plot(year, lynxes, color = "red")
    # plt.plot(year, hare_dying, color = "green")
    # plt.xticks(x_years)
    #
    # plt.legend(["Lynxes", "hare death rate"])
    # plt.show()

    """
    plot 3
    """
    # hare_dying = np.gradient(hares, 1)
    # cor = np.corrcoef(hare_dying, lynxes)[0, 1]
    # plt.title("relation between lynx population and the hare death rate")
    # plt.ylabel("Hare birth rate")
    # plt.xlabel("Lynxes")
    # plt.scatter(lynxes, hare_dying)
    # plt.show()

print(editing_file("populations.txt"))

