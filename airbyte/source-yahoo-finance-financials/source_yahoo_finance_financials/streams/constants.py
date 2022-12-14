BROWSER_HEADERS = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)",
}  # Required to avoid 403 response (thank you thorn)

BALANCE_TYPE_PARAMETERS = [
    "StockholdersEquity",
    "PrepaidAssets",
    "CashAndCashEquivalents",
    "InvestmentinFinancialAssets",
    "GoodwillAndOtherIntangibleAssets",
    "AdditionalPaidInCapital",
    "TotalTaxPayable",
    "CommonStockEquity",
    "CashFinancial",
    "TangibleBookValue",
    "ShareIssued",
    "CapitalStock",
    "OtherPayable",
    "CurrentAssets",
    "TotalCapitalization",
    "CurrentLiabilities",
    "NetPPE",
    "MachineryFurnitureEquipment",
    "AccumulatedDepreciation",
    "OtherShortTermInvestments",
    "TreasuryStock",
    "TreasurySharesNumber",
    "FinancialAssetsDesignatedasFairValueThroughProfitorLossTotal",
    "DividendsPayable",
    "RetainedEarnings",
    "CommonStock",
    "OrdinarySharesNumber",
    "WorkingCapital",
    "AssetsHeldForSaleCurrent",
    "TaxesReceivable",
    "TotalLiabilitiesNetMinorityInterest",
    "CashCashEquivalentsAndShortTermInvestments",
    "TotalAssets",
    "InvestedCapital",
    "Payables",
    "AccountsPayable",
    "RestrictedCash",
    "TotalEquityGrossMinorityInterest",
    "TotalNonCurrentAssets",
    "GrossPPE",
    "OtherReceivables",
    "NetTangibleAssets",
    "Receivables",
    "LongTermDebt",
    "TotalDebt",
    "Goodwill",
    "FinancialAssets",
    "AccountsReceivable",
    "PreferredStock",
    "NetDebt",
    "CashEquivalents",
    "CurrentDebt",
]

INCOME_TYPE_PARAMETERS = [
    "TotalRevenue",
    "CostOfRevenue",
    "GrossProfit",
    "OperatingExpense",
    "EBIT",
    "EBITDA",
    "NetIncome",
    "NetIncomeCommonStockholders",
    "OperatingRevenue",
    "ResearchAndDevelopment",
    "Amortization",
    "OperatingIncome",
    "TotalExpenses",
    "BasicEPS",
    "BasicAverageShares",
]

CASHFLOW_TYPE_PARAMETERS = [
    "FreeCashFlow",
    #    "OtherNonCashItems",
    #    "InvestingCashFlow",
    #    "LongTermDebtIssuance",
    #    "InterestReceivedCFI",
    #    "DepreciationAndAmortization",
    #    "OperatingCashFlow",
    #    "PurchaseOfInvestment",
    #    "StockBasedCompensation",
    #    "NetIncomeFromContinuingOperations",
    #    "SaleOfInvestment",
    #    "Depreciation",
    #    "CommonStockPayments",
    #    "ChangeInReceivables",
    #    "NetCommonStockIssuance",
    #    "ChangeInWorkingCapital",
    #    "NetInvestmentPurchaseAndSale",
    #    "EffectOfExchangeRateChanges",
    #    "GainLossOnSaleOfPPE",
    #    "CashDividendsPaid",
    #    "BeginningCashPosition",
    #    "PurchaseOfPPE",
    #    "LongTermDebtPayments",
    #    "IssuanceOfDebt",
    #    "OtherCashAdjustmentOutsideChangeinCash",
    #    "FinancingCashFlow",
    #    "GainLossOnInvestmentSecurities",
    #    "RepurchaseOfCapitalStock",
    #    "SaleOfBusiness",
    #    "CapitalExpenditure",
    #    "NetIssuancePaymentsOfDebt",
    #    "NetIntangiblesPurchaseAndSale",
    #    "CommonStockIssuance",
    #    "RepaymentOfDebt",
    #    "NetBusinessPurchaseAndSale",
    #    "DividendsReceivedCFI",
    #    "ChangesInCash",
    #    "IssuanceOfCapitalStock",
    #    "NetForeignCurrencyExchangeGainLoss",
    #    "NetOtherInvestingChanges",
    #    "NetLongTermDebtIssuance",
    #    "PurchaseOfIntangibles",
    #    "ChangeInPayable",
    #    "EndCashPosition",
    #    "ChangeInOtherCurrentAssets",
    #    "CommonStockDividendPaid",
    #    "NetPPEPurchaseAndSale",
    #    "SaleOfPPE",
    #    "TaxesRefundPaid",
    #    "Depletion",
    #    "ProceedsFromStockOptionExercised",
    #    "ChangeInInterestPayable",
    #    "CashFlowFromContinuingInvestingActivities",
    #    "ShortTermDebtPayments",
    #    "DividendPaidCFO",
    #    "PurchaseOfBusiness",
    #    "PaymentsonBehalfofEmployees",
    #    "InterestPaidCFF",
    #    "SaleOfIntangibles",
    #    "TaxesRefundPaidDirect",
    #    "PensionAndEmployeeBenefitExpense",
    #    "CashFromDiscontinuedOperatingActivities",
    #    "ChangeInPrepaidAssets",
    #    "PaymentstoSuppliersforGoodsandServices",
    #    "DomesticSales",
    #    "InterestPaidCFO",
    #    "NetShortTermDebtIssuance",
    #    "ClassesofCashPayments",
    #    "SaleOfInvestmentProperties",
    #    "DividendReceivedCFO",
    #    "OtherCashPaymentsfromOperatingActivities",
    #    "PreferredStockDividendPaid",
    #    "ChangeInAccruedExpense",
    #    "CashFlowFromDiscontinuedOperation",
    #    "ChangeInPayablesAndAccruedExpense",
    #    "CashFlowFromContinuingOperatingActivities",
    #    "AdjustedGeographySegmentData",
    #    "OtherCashReceiptsfromOperatingActivities",
    #    "NetPreferredStockIssuance",
    #    "CapitalExpenditureReported",
    #    "AmortizationCashFlow",
    #    "ChangeInAccountPayable",
    #    "DividendsPaidDirect",
    #    "OperatingGainsLosses",
    #    "UnrealizedGainLossOnInvestmentSecurities",
    #    "AssetImpairmentCharge",
    #    "ChangeInInventory",
    #    "ExcessTaxBenefitFromStockBasedCompensation",
    #    "PreferredStockPayments",
    #    "ForeignSales",
    #    "PurchaseOfInvestmentProperties",
    #    "ShortTermDebtIssuance",
    #    "AmortizationOfIntangibles",
    #    "ReceiptsfromGovernmentGrants",
    #    "ChangesInAccountReceivables",
    #    "PreferredStockIssuance",
    #    "CashFromDiscontinuedFinancingActivities",
    #    "InterestReceivedCFO",
    #    "IncomeTaxPaidSupplementalData",
    #    "NetOtherFinancingCharges",
    #    "ChangeInTaxPayable",
    #    "ChangeInOtherCurrentLiabilities",
    #    "ChangeInIncomeTaxPayable",
    #    "CashFlowsfromusedinOperatingActivitiesDirect",
    #    "InterestPaidDirect",
    #    "ClassesofCashReceiptsfromOperatingActivities",
    #    "ProvisionandWriteOffofAssets",
    #    "EarningsLossesFromEquityInvestments",
    #    "GainLossOnSaleOfBusiness",
    #    "ChangeInDividendPayable",
    #    "DeferredIncomeTax",
    #    "DividendsReceivedDirect",
    #    "AmortizationOfSecurities",
    #    "CashFlowFromContinuingFinancingActivities",
    #    "OtherCashAdjustmentInsideChangeinCash",
    #    "InterestReceivedDirect",
    #    "NetInvestmentPropertiesPurchaseAndSale",
    #    "CashFromDiscontinuedInvestingActivities",
    #    "DepreciationAmortizationDepletion",
    #    "ChangeInOtherWorkingCapital",
    #    "ReceiptsfromCustomers",
]

COMPANY_TYPE_PARAMETERS = []

OWNERSHIP_TYPE_PARAMETERS = []

from datetime import datetime
from dateutil.relativedelta import relativedelta

TODAY = datetime.today()
FIVE_YEARS = relativedelta(years=5)
FIVE_YEARS_AGO = TODAY - FIVE_YEARS

PERIOD1 = int(FIVE_YEARS_AGO.timestamp())
PERIOD2 = int(TODAY.timestamp())