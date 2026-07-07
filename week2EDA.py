import pandas as pd
import matplotlib.pyplot as plt

soldDf = pd.read_csv("CRMLSSoldCombinedResidential.csv")
listingsDf = pd.read_csv("CRMLSListingCombinedResidential.csv")


print("SOLD")
print("-"*35)
print(f"Rows: {soldDf.shape[0]:,}")
print(f"Columns: {soldDf.shape[1]}")

print("LISTINGS")
print("-"*35)
print(f"Rows: {listingsDf.shape[0]:,}")
print(f"Columns: {listingsDf.shape[1]}")


print("Column Names:")
print(soldDf.columns.tolist())
print("dtypes:", soldDf.dtypes)


#should just return residential if we are using post-filt
print(soldDf["PropertyType"].unique())
########################################################################################################################################
# Missing Data Analysis
########################################################################################################################################
# -----------------------------
# SOLD DATASET
# -----------------------------

missingCountSeries = soldDf.isnull().sum()
missingPercentSeries = (missingCountSeries / len(soldDf)) * 100

missingReport = pd.DataFrame({
    "Missing Count": missingCountSeries,
    "Missing Percent": missingPercentSeries.round(2)
}).sort_values("Missing Percent", ascending=False)

# Find columns with more than 90% missing values

over90 = missingReport[missingReport["Missing Percent"] > 90]
# over90 = missingReport[missingReport.iloc[:, 1] > 90]

print("\nSOLD columns with over 90% missing:")
print(over90)

# Saving the reports
missingReport.to_csv("sold_missing_report.csv")
over90.to_csv("sold_over90.csv")

# dropping vs retaining columns
soldColsToDrop = over90.index.tolist()

print("\nDropping these SOLD columns:")
for col in soldColsToDrop:
    print(",", col)

# Drop columns
soldDf = soldDf.drop(columns=soldColsToDrop)

print(f"\nSOLD columns remaining: {soldDf.shape[1]}")


# -----------------------------
# LISTINGS DATASET (SAME PROCES AS SOLD)
# -----------------------------

listingMissingCountSeries = listingsDf.isnull().sum()
listingMissingPercentSeries = (listingMissingCountSeries / len(listingsDf)) * 100

listingMissingReport = pd.DataFrame({
    "Missing Count": listingMissingCountSeries,
    "Missing Percent": listingMissingPercentSeries.round(2)
}).sort_values("Missing Percent", ascending=False)

# Find columns with more than 90% missing values
listingOver90 = listingMissingReport[
    listingMissingReport["Missing Percent"] > 90
]

print("\nLISTINGS columns with over 90% missing:")
print(listingOver90)

# Save reports
listingMissingReport.to_csv("listings_missing_report.csv")
listingOver90.to_csv("listings_over90.csv")

# Store column names to drop
listingColsToDrop = listingOver90.index.tolist()

print("\nDropping these LISTINGS columns:")
for col in listingColsToDrop:
    print("-", col)

# Drop columns
listingsDf = listingsDf.drop(columns=listingColsToDrop)

print(f"\nLISTINGS columns remaining: {listingsDf.shape[1]}")


####################################################################
# Save Cleaned Datasets
####################################################################

soldDf.to_csv("CRMLSSoldCleaned.csv", index=False)
listingsDf.to_csv("CRMLSListingCleaned.csv", index=False)

print("\nCleaned datasets saved successfully!")

###############################
# EDA
###############################

#---------- Q1: residential vs other?

rawListings = pd.read_csv("rawListings.csv")
rawSold = pd.read_csv("rawSold.csv")
##
listingCounts = rawListings["PropertyType"].value_counts(dropna=False)
listingShare = (listingCounts / len(rawListings) * 100).round(2)

print("********************************")
print("Residential share (vs other)", listingShare)
print("********************************")

#---------- Q2: median and avg closing price?

print("\n********************************")
print("Close Price Statistics")
print("********************************")

print(f"Average Close Price: ${soldDf['ClosePrice'].mean():,.3f}")
print(f"Median Close Price:  ${soldDf['ClosePrice'].median():,.3f}")

#---------- Q3: days on market distribution
print("\n********************************")
print("Days on Market Distribution Info")
print("********************************")
daysOnMarketDf = soldDf["DaysOnMarket"].describe().loc[["std", "min", "25%", "50%", "75%", "max", "mean"]]
daysOnMarketDf.loc["IQR"] = daysOnMarketDf.loc["75%"]-daysOnMarketDf.loc["25%"]
print(daysOnMarketDf)

# histogram time!

plt.hist(
    soldDf["DaysOnMarket"].dropna(),
    bins=25,
    edgecolor="black"
)

plt.title("Days on Market Distribution")
plt.xlabel("Days on Market")
plt.ylabel("Number of Houses")

plt.show()


# ------just doing all histograms at once here

numericCols = [
    "ClosePrice",
    "ListPrice",
    "OriginalListPrice",
    "LivingArea",
    "LotSizeAcres",
    "BedroomsTotal",
    "BathroomsTotalInteger",
    "DaysOnMarket",
    "YearBuilt"
]

for col in numericCols:

    plt.hist(
        soldDf[col].dropna(),
        bins=25,
        edgecolor="black"
    )

    plt.title(f"{col} Distribution")
    plt.xlabel(col)
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.savefig(f"{col}_histogram.png")
    plt.show()


# --------and also making all boxplots at once

for col in numericCols:

    plt.boxplot(
        soldDf[col].dropna(),
        vert=False
    )

    plt.title(f"{col} Boxplot")
    plt.xlabel(col)
    plt.tight_layout()
    plt.savefig(f"{col}_boxplot.png")
    plt.show()