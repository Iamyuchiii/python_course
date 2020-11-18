import scipy.cluster.hierarchy as sch
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

def parsing_data(filename):
    with open(filename, "r") as data:
        parse = {}
        headers = {}
        for index, line in enumerate(data):
            if index == 0:
                headerline = line.strip().split("\t")
                for index, header in enumerate(headerline[1:]):
                    headers[index] = header
            else:
                clean_line = line.strip().split("\t")
                if clean_line[0] not in parse:
                    parse[clean_line[0]] = clean_line[1:]
        return  parse, headers

def pandaframe_transform(dictionary, headers):
    dataframe = pd.DataFrame.from_dict(dictionary)
    # changing name
    dataframe = dataframe.rename(index = headers)
    return dataframe

def hierarchical_clustering(dataframe, headers):
    header_list = list(dataframe)
    dataframe = dataframe.transpose()
    # pairwise distance
    distances = sch.distance.pdist(dataframe, metric="euclidean")
    clustering = sch.linkage(distances, method="complete")
    tree = sch.dendrogram(clustering, color_threshold=25, labels=dataframe.index.values)

    # nieuw tree
    distances_2 = sch.distance.pdist(dataframe, metric="correlation")
    clustering_2 = sch.linkage(distances_2, method="complete")
    tree_2 = sch.dendrogram(clustering_2, leaf_font_size=2, color_threshold=4, labels=header_list)


def heatmap_clustering(dataframe):
    dataframe = dataframe.transpose()
    dataframe = dataframe.astype(float)
    heat_map = sns.clustermap(dataframe)
    plt.show()

if __name__ == "__main__":
    dictionary, headers = parsing_data("Clustering_data.txt")
    dataframe = pandaframe_transform(dictionary, headers)
    hierarchical_clustering(dataframe, headers)
    heatmap_clustering(dataframe)