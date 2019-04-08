# -*- coding: utf-8 -*-
# MySQL Workbench Python script
# MySql Workbench Reporting Script
# Written in MySQL Workbench 8.0
# Auther chali5124@gmail.com

def is_primary(entrys, value):
    for entry in entrys:
            if entry.indexType == "PRIMARY":
                for en in entry.columns:
                    if en.referencedColumn.name == value:
                        return "Y"

    return ""

def is_unique(entrys, value):
    for entry in entrys:
        if entry.indexType == "UNIQUE":
            if len(entry.columns) == 1:
                for en in entry.columns:
                    if en.referencedColumn.name == value:
                        return "Y"

    return ""

def is_set(param):
    if param == 1:
        return "Y"
    else:
        return ""

def is_binary(entrys):
    if "BINARY" in entrys:
        return "Y"
    else:
        return ""

def is_unsigned(entrys):
    if "UNSIGNED" in entrys:
        return "Y"
    else:
        return ""

def is_zerofill(entrys):
    if "ZEROFILL" in entrys:
        return "Y"
    else:
        return ""

def get_headerget_header(table, comment):
    html = "<table width='100%' border='1' cellspacing='0' cellpadding='0'>\n"
    html += "\t<thead>\n"
    html += "\t\t<tr><th colspan='11'>" + table + "</th></tr>\n"

    if comment :
        html += "\t\t<tr><th colspan='11'>" + comment + "</th></tr>\n"

    html += "\t<tr><th width='15%'>Name</th><th width='10%'>Data Type</th><th width='2%'>PK</th><th width='2%'>NN</th><th width='2%'>UQ</th><th width='2%'>BIN</th><th width='2%'>UN</th><th width='2%'>ZF</th><th width='2%'>AI</th><th width='15%'>Default</th><th width='*'>Comment</th></tr>\n"
    html += "\t</thead>\n"
    html += "\t<tbody>\n"
    return html

def get_footer():
    html = ""
    html += "\t</tbody>\n"
    html += "</table>"
    html += "</div></body></html>"
    return html

try:
    schema = grt.root.wb.doc.physicalModels[0].catalog.schemata[1]
    files = open("/Users/leechanrin/Downloads/report.html", "w")
    files.write("<html><head>")
    files.write("<meta charset=\"utf-8\"><meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no\">")
    files.write("<style>table,th,td{border:solid 1px #ddd;font-family:arial,serif;}table{margin-bottom:20px;border-collapse:collapse;border-spacing:0;}th{background:#efefef;text-align:center;padding:15px;}td{padding:15px;}</style>")
    files.write("<html><head><meta charset=\"utf-8\"><style>table,th,td{border:solid 1px #ddd;font-family:arial,serif;}table{margin-bottom:20px;border-collapse:collapse;border-spacing:0;}th{background:#efefef;text-align:center;padding:15px;}td{padding:15px;}</style></head><body>")
    files.write("<body><div class=\"container\">")

    for table in schema.tables:
        files.write(get_header(table.name, table.comment))
        for column in table.columns:
            files.write("\t\t<tr>")
            files.write("<td>" + column.name + "</td>")
            files.write("<td>" + column.formattedType + "</td>")
            files.write("<td>" + is_primary(table.indices, column.name) + "</td>")
            files.write("<td>" + is_set(column.isNotNull) + "</td>")
            files.write("<td>" + is_unique(table.indices, column.name) + "</td>")
            files.write("<td>" + is_binary(column.flags) + "</td>")
            files.write("<td>" + is_unsigned(column.flags) + "</td>")
            files.write("<td>" + is_zerofill(column.flags) + "</td>")
            files.write("<td>" + is_set(column.autoIncrement) + "</td>")
            files.write("<td>" + column.defaultValue + "</td>")
            files.write("<td>" + column.comment + "</td>")
            files.write("\t\t</tr>\n")

        files.write(get_footer())
    files.close()
    print "Complete! "
except IOError:
    print "Error"
