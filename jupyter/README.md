=====Python 3 Via Jupyter Notebook=====

====Random notes====

1. Browsing .ipynb files on github is *great*, but none of the input() functions will, erm, function. See INSTALL.md, using anaconda to install jupyter, and cloning the .ipynb files from github to your workstation. 

1. Each pupil runs their own notebook server. Put all the .ipynb files in one shared network folder (Pool) and set that folder to be read only for pupils. If  using Anaconda Prompt on windows, right click the Anaconda icon and change the target directory to be that of the shared pool folder. On typical corporate network setups, you will need to authenticate as superuser to change the folder target.

1. For a permanent record, consider getting pupils to print (CTRL-P) their finished notebook pages to a physical printer or PDF output.

1. Hit CTRL-Enter to run interactive cells. If an input() is required, you just type you entry and press plain old Enter. Individual cell outputs can be cleared via the Cell menu.

1. A pupil may report that a bit of interactive Python won't run. Each notebook can only have one running cell. Check above and below to ensure the pupil has finished interacting with other cells.

1. A pupil may inadvertently type into an interactive cell and trash it. CTRL-z works to undo. Or just reload the entire page (which will work because you set it to read only, right? :) ). Each page is quite small in terms of time effort and repeating a little won't do any harm at all.

1. A pupil may accidentally create a blank cell. You can ignore it, or delete it by pressing ESCape, then X. 
