# --------------------------------------------------------------------------

# Kernel Density Plot
sns.displot(us_salaries['salary'],
            kde=True, 
            bins=6)




# --------------------------------------------------------------------------

# Joint Grid, KDE Plot
joint = sns.JointGrid(data=subset,
                      x="mintemp",
                      y="windgustspeed")

joint = joint.plot_joint(sns.kdeplot)


joint = joint.plot_marginals(sns.kdeplot, 
                             shade=True)




# --------------------------------------------------------------------------

# Regression Plot for Categorical Variable
sns.regplot(data=state_unemployment,
            x="month",
            y="unemployment_rate",
            order=2,
            size="average_salary")



# Polynomial Regression
sns.regplot(data=climate_change, 
            x='relative_temp', 
            y='co2', 
            order=4)




# -----------------------------------------------------------------

sns.relplot(x="age",
            y="rating",
            data=fifa_subset,
            kind="line")




# -----------------------------------------------------------------

# See the difference in preferred foot used in soccer based on nationality
sns.countplot(x="nationality",
              hue="preferred_foot",
              data=fifa_chelsea)




# -----------------------------------------------------------------

sns.violinplot(data=state_unemployment, 
               y="Date",
               x="Unemployment_Rate",
               palette="Paired")




# -----------------------------------------------------------------

# Add Dashed Line
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey=True)
sns.histplot(use_unemployment.Men, ax=ax0)
Rsns.histplot(use_unemployment.Women, ax=ax1)
ax1.axvline(x=5, label='Rate 5.0', linestyle='--')

plt.show()



# -----------------------------------------------------------------
