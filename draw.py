import matplotlib.pyplot as plt


def draw(datas, xtick, ytick, xlabel, ylabel, legends, savepdf):
    curve_num=len(datas)
    #plt.rc('text', usetex=True)
    col_list=['r','g','b']
    ls=['-', '--', '-.']
    ms=['s','d','o']
    plt.figure(figsize=(10,7))
    for i in range(curve_num):
        assert len(datas[i])==len(xtick)
    
    plt.axis([1,len(xtick),ytick[0],ytick[-1]])
    for i in range(curve_num):
        plt.plot([i for i in range(1,len(xtick)+1)], datas[i],c=col_list[i], linewidth=4,markersize = 10,marker=ms[i],linestyle=ls[i],label=legends[i])
    plt.xticks([i for i in range(1,1+len(xtick))], [str(x) for x in xtick], fontsize=20)
    plt.yticks([ytick[i] for i in range(len(ytick))], fontsize=20)
    plt.xlabel(xlabel, fontsize=20)
    plt.ylabel(ylabel, fontsize=20)
    plt.legend(legends, fontsize=20)
    plt.grid()
    plt.savefig(savepdf)
    #line thicker, legend

xscale=[0.0001,0.001,0.01]
data=[[0.252,0.253,0.312],[0.293,0.292,0.326],[0.27,0.272,0.303]]
draw(data, xscale, [0.0,0.1,0.2,0.3,0.4], 'Guassian noise $\sigma$' ,'Pixel Accuracy',['PSPNet','PSANet','HRNet-OCR'], 'exp1_voc.pdf')

data=[[0.099,0.098,0.105],[0.11,0.111,0.134],[0.227,0.227,0.252]]
draw(data, xscale, [0.0,0.1,0.2,0.3,0.4], 'Guassian noise $\sigma$' ,'Pixel Accuracy',['PSPNet','PSANet','HRNet-OCR'], 'exp1_cityscape.pdf')

data=[[0.188,0.19,0.238],[0.139,0.14,0.168],[0.215,0.213,0.242]]
draw(data, xscale, [0,0.1,0.2,0.3,0.4], 'Guassian noise $\sigma$' ,'Pixel Accuracy',['PSPNet','PSANet','HRNet-OCR'], 'exp1_ade20k.pdf')