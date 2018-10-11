# Visualizing Flight Test Data Interactively With Open Source Tools

Notebooks for talk given in October 2018 at the Society of Flight Test Engineers (SFTE) Symposium in Savannah, GA. 

- - -

[Presentation Notebook](/sfte2018.ipynb) | [Paper](/paper/Visualizing Flight Test Data Interactively With Open Source Tools.pdf)


# Intro
Much of the flight test community relies on proprietary tools for data analysis. These tools can be expensive and create a “vendor lock” problem. Configuring a tool or tool chain for a specific use case will always require a fair amount of up-front work. This can include adding the understanding of file and message formats, defining the relationships and levels of aggregation between the different data products, and creating visualizations specific to a project’s goals. If this configuration work is performed within a “walled garden” then the team can become locked in as the cost to exit the specific tool or tool chain becomes higher the longer the team uses the tooling. This is because, over time, more and more project specific information is defined within the walled-off space. Extrication can prove difficult. 

The good news is that there is an alternative. Robust open source tools exist to store, transform, and visualize flight test data. This paper makes the case that open source tools are a superior choice for today’s flight test analysis problems. These tools utilize open interfaces, which has led to widespread compatibility across scores of tools and ensures seamless migration between tools (no “vendor lock”). The openness and the compatibility it facilitates has created a community of interoperable tools. This allows for the flexibility and agility to tailor tooling to a specific project’s needs rather than being forced to use a singular proprietary tool whether it suits the job at hand or not because that is where all the previous work has been done. 

This paper includes a case study where Open Flight Data is stored, transformed, and visualized using open source tools. The data is publicly available flight data, primarily from Automatic Dependent Surveillance-Broadcast (ADS-B). This case study utilized a specific suite of open source tools although the arguments for their use are valid for other open source alternatives. This suite includes the Hierarchical Data Format 5 (HDF5), Pandas, Luigi, Jupyter, Bokeh, and Datashader. This suite of tools either are all Python based or work well with Python. Python is a popular scripting language used in scientific computing and is currently the fastest growing major programming language.[1]  These tools are discussed in detail in the following sections. 

[1] David Robinson, “The Incredible Growth of Python,” The Stack Overflow Blog, September 6, 2017, https://stackoverflow.blog/2017/09/06/incredible-growth-python.
