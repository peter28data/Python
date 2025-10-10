# --------------------------------------------------------------------------

# Kernel Density Plot
sns.displot(us_salaries['salary'],
            kde=True, 
            bins=6)





# --------------------------------------------------------------------------

# Joint Grid using KDE Plot
joint = sns.JointGrid(data=subset,
                      x="mintemp",
                      y="windgustspeed")

joint = joint.plot_joint(sns.kdeplot)


joint = joint.plot_marginals(sns.kdeplot, 
                             shade=True)
plt.show()





# --------------------------------------------------------------------------

# Regression Plot for Categorical Variable
sns.regplot(data=state_unemployment,
            x="month",
            y="unemployment_rate",
            order=2)
