
import pandas as pd
# Listings


listings = pd.concat([
    pd.read_csv("CRMLSListing202403.csv"),
    pd.read_csv("CRMLSListing202404.csv"),
    pd.read_csv("CRMLSListing202405.csv"),
    pd.read_csv("CRMLSListing202406.csv"),
    pd.read_csv("CRMLSListing202407.csv"),
    pd.read_csv("CRMLSListing202408.csv"),
    pd.read_csv("CRMLSListing202409.csv"),
    pd.read_csv("CRMLSListing202410.csv"),
    pd.read_csv("CRMLSListing202411.csv"),
    pd.read_csv("CRMLSListing202412.csv"),
    pd.read_csv("CRMLSListing202501.csv"),
    pd.read_csv("CRMLSListing202502.csv"),
    pd.read_csv("CRMLSListing202503.csv"),
    pd.read_csv("CRMLSListing202504.csv"),
    pd.read_csv("CRMLSListing202505.csv"),
    pd.read_csv("CRMLSListing202506.csv"),
    pd.read_csv("CRMLSListing202507.csv"),
    pd.read_csv("CRMLSListing202508.csv"),
    pd.read_csv("CRMLSListing202509.csv"),
    pd.read_csv("CRMLSListing202510.csv"),
    pd.read_csv("CRMLSListing202511.csv"),
    pd.read_csv("CRMLSListing202512.csv"),
    pd.read_csv("CRMLSListing202601.csv"),
    pd.read_csv("CRMLSListing202602.csv"),
    pd.read_csv("CRMLSListing202603.csv"),
    pd.read_csv("CRMLSListing202604.csv"),
   # pd.read_csv("CRMLSListing202605.csv"),
   # pd.read_csv("CRMLSListing202606.csv")
], ignore_index=True)

print("num of listings rows pre-filt:", len(listings))
listings = listings[listings["PropertyType"] == "Residential"]
print("num of listings rows post-filt:", len(listings))

# sold
sold = pd.concat([
    pd.read_csv("CRMLSSold202403.csv"),
    pd.read_csv("CRMLSSold202404.csv"),
    pd.read_csv("CRMLSSold202405.csv"),
    pd.read_csv("CRMLSSold202406.csv"),
    pd.read_csv("CRMLSSold202407.csv"),
    pd.read_csv("CRMLSSold202408.csv"),
    pd.read_csv("CRMLSSold202409.csv"),
    pd.read_csv("CRMLSSold202410.csv"),
    pd.read_csv("CRMLSSold202411.csv"),
    pd.read_csv("CRMLSSold202412.csv"),
    pd.read_csv("CRMLSSold202501.csv"),
    pd.read_csv("CRMLSSold202502.csv"),
    pd.read_csv("CRMLSSold202503.csv"),
    pd.read_csv("CRMLSSold202504.csv"),
    pd.read_csv("CRMLSSold202505.csv"),
    pd.read_csv("CRMLSSold202506.csv"),
    pd.read_csv("CRMLSSold202507.csv"),
    pd.read_csv("CRMLSSold202508.csv"),
    pd.read_csv("CRMLSSold202509.csv"),
    pd.read_csv("CRMLSSold202510.csv"),
    pd.read_csv("CRMLSSold202511.csv"),
    pd.read_csv("CRMLSSold202512.csv"),
    pd.read_csv("CRMLSSold202601.csv"),
    pd.read_csv("CRMLSSold202602.csv"),
    pd.read_csv("CRMLSSold202603.csv"),
    pd.read_csv("CRMLSSold202604.csv"),
 #  pd.read_csv("CRMLSSold202605.csv"),
  #  pd.read_csv("CRMLSSold202606.csv")
], ignore_index=True)
print("num of sold rows pre-filt:", len(sold))
sold = sold[sold["PropertyType"] == "Residential"]
print("num of sold rows post-filt:", len(sold))
