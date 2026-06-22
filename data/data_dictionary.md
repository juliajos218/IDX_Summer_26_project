# Key Columns in Data
## Targets and Filters:
  - ClosePrice - decimal, the amount of money paid by the purchaser to the seller for the property
  - PropertyType - Enum, list of properties (NOTE: we restrict this to "Residential")
  - PropertySubType - Enum, list of subtypes (NOTE: we rescrict this to "SingleFamilyResidence")
  - StandardStatus - Enum, status of the listing in the state of the contract (active, active under contract, canceled, closed, expired, pending, withdrawn)

  # Features:
    - LivingArea - decimal, total livable area within structure
    - LivingAreaUnits - enum, pick list of unit measurement for the area
    - BedroomsTotal- int32, number of bedrooms in dwelling
    - BathroomsTotal - int32, simple sum of the number of bathrooms (if half bath counted as 1)
    - BathroomsFull - int32, room containing 4 elements: toilet, sink, tub, shower head
    - BathroomsHalf - int32, room containing 2/4 elements listed above
    - LotSizeSquareFeet - decimal, total square footage of the lot
    - LotSizeUnits- enum, list of measurements for the area (must be in alignment of other measurements)
    - YearBuilt - int32, year that an occupancy permit is first granted for the house or other local measure of initial habitability of the build

  # Locations:
    - Latitude - decimal, geographic latitude
    - Longitude - decimal, geographic longtitude
    - City - string, city in listing address
    - ElementarySchoolDistrict - string, name of elementary school district having a catchmnet that includes property
    - HighSchoolDistrict - string, name of high school district having a catchmnet that includes property

  # Dates:
    - CloseDate - DateTime, the date the purchase agreement was fulfilled for sale listings, for lease listings it is the date the requirements were fulfilled
    - OnMarketDate - DateTime, date the listing was placed on market
    - DaysOnMarket - Int32, number of days the listing is on market

  # Other:
    - TaxAnnualAmmount - Decimal, annual property tax amount as of the last assessment
    - TaxAssessedValue - int32, property value as of the last assessment
    - Zoning - string, list of descriptions of the zoning of the property
