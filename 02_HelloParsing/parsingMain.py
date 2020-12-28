import orderParsingModule

kccExcelSrc = "orderExcel/KCC/report_KCC.xls"
kccCsvSrc   = "orderCsv/KCC/report_KCC.csv"

m3EocSrc    = "orderEoc/3M/report_3M.eoc"

# orderParsingModule.xls2Csv(kccExcelSrc, kccCsvSrc)
# content = orderParsingModule.csv2String(kccCsvSrc, ',')
# order = orderParsingModule.string2ObjectForKCC(content)

# print(order)

content = orderParsingModule.eoc2String(m3EocSrc, '\t')
order = orderParsingModule.string2ObjectFor3M(content)

print(order)