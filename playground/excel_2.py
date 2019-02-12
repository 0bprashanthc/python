import xlrd

kpi_data = {
    'MME': {
        'MME_Inter_Tracking':'InterMMETrackingAreaUpdateSuccessRateLF',
        'MME_Intra_Tracking':'Column',
        'MME_S1AP_NAS_TRANSPORT':'Column_name',
        'MME_PS_Paging_Success_Rate':'Column_name',
        'MME_S1_Intra_Success':'Column_name',
        'MME_CSFB_MT_Voice_Success':'Column_name',
        'MME_S1_Inter_Success':'Column_name',
        'MME_EMM_SIGNALING':'Column_name',
        '3G_Attach_Success_Rate':'Column_name',
        'MME_CSFB_MO_SMS_Success':'Column_name',
        'MME_PAGING_LAST':'Column_name',
        'MME_Overall_Success':'Column_name',
        'MME_CSFB_MO_Voice_Success':'Column_name',
        'MME_INTRA':'Column_name',
        'MME_INTRA_XMODE':'Column_name',
        '2G_PDP_Context_Activation':'Column_name',
        'MME_KPI_STATISTICS':'Column_name',
        '3G_PDP_Activation_Success':'Column_name',
        'MME_EMM_SIGNALING':'Column_name'
        },
    'SGW': {
        'SGW_PAGING_KPI':'Requests',
        'SGW_DOWNLINK_TOTAL_DROPPED_PACKET_KPI':'Column_name',
        'SGW_DEDICATED_KPI':'Column_name',
        'SGW_SESSIONS_PDN_KPI':'Column_name',
        'SGW_TOTAL_EPS_BEARERS_KPI':'Column_name',
        'SGW_S1U_DOWNLINK_KPI':'Column_name',
        'SGW_S5S8_DOWNLINK_KPI':'Column_name',
        'SGW_UPLINK_TOTAL_DROPPED_PACKET_KPI':'Column_name',
        'SGW_TOTAL_BEARER_ACTIVE_KPI':'Column_name',
        'SGW_HANDOVER_KPI':'Column_name',
        'SGW_UPLINK_KPI':'Column_name',
        'SGW_PLMN_KPI':'Column_name',
        'SGW_SESSIONS_KPI':'Column_name',
        'SGW_S5S8_UPLINK_KPI':'Column_name',
        'SGW_HANDOVER_II_KPI':'Column_name',
        'SGW_S1U_UPLINK_KPI':'Column_name',
        'SGW_DOWNLINK_TOTAL_KPI':'Column_name'
        },
    'PGW':{
        'PGW_APN_AMBR_KPI':'Column_name',
        'PGW_BEARER_ACTIVE_RATE_KPI':'Column_name',
        'PGW_SESSION_ADDRESS_KPI':'Column_name',
        'PGW_HANDOVER_SUCCRATE_KPI':'Column_name',
        'PGW_THROUGHPUT':'Column_name',
        'PGW_TOT_DOWN_BYTES_FWD_KPI':'Column_name',
        'PGW_BEARER_REJ':'Column_name',
        'PGW_HANDOVERSTAT_KPI':'Column_name',
        'PGW_SUB_KPI':'Column_name',
        'PGW_KPI_STATISTICS':'Column_name',
        'PGW_SESSION_PDN_KPI':'Column_name',
        'PGW_SUB_DOWN_PACKET_DROP_KPI':'Column_name',
        'PGW_SESSION_RELEASED_KPI':'Column_name',
        'PGW_TOT_DOWN_PKTS_FWD_KPI':'Column_name',
        'PGW_SUB_SGI_KPI':'Column_name',
        'PGW_TOT_UP_BYTES_FWD_KPI':'Column_name',
        'PGW_SESSION_ACTIVE_KPI':'Column_name',
        'PGW_SESSION_MODIFIED_QOS_KPI':'Column_name',
        'PGW_SESSION_REJECTED_KPI':'Column_name',
        'PGW_TOT_UP_PKT_FWD_KPI':'Column_name',
        'PGW_SESSION_MODIFIED_KPI':'Column_name',
        'PGW_SUB_UP_PACKET_DROP_KPI':'Column_name'
        },
    'SGSN':{
        'SGSN_RAB_KPI':'Column_name',
        'SGSN_IMSI_KPI':'Column_name',
        'SGSN_2G_INTRA_RAU_SUCCESS':'Column_name',
        'SGSN_2G_INTER_SGSN_RAU_SUCCESS':'Column_name',
        'SGSN_3G_Inter_SGSN_RAU_Success_Rate':'Column_name',
        'SGSN_3G_Intra_SGSN_RAU_Success_Rate':'Column_name'
        },
    'GGSN':{
        'GGSN_KPI':'Column_name'
        }
    }

def get_kpi_data(daily_report, kpi_name, column_name):
    '''
        1. open $daily_report excel sheet
        2. goto $kpi_name sheet
        3. goto $column_name
        4. calculate average and maximum of all rows for column
    '''
    #open excel sheet
    excel_file = xlrd.open_workbook(daily_report)
    #goto kpi sheet
    kpi_data = excel_file.sheet_by_name(kpi_name)
    #number of values/rows for kpi
    number_of_values = int(kpi_data.nrows)-1
    #column-names in kpi sheet
    columns = kpi_data.row_values(0)
    index_, values = None, []
    for column_index in range(len(columns)):
        #read only one column
        if str(columns[column_index]).upper() == column_name.upper():
            index_ = column_index
    if index_ is not None:
        for each_row in range(1,number_of_values+1):
            #get all rows for that column
            values.append(float(kpi_data.row_values(each_row)[index_]))
    #calculate average and maximum
    average, maximum = sum(values)/float(len(values)) , max(values)
    return (average,maximum)

def write_to_excel_template(daily_data):
    '''
       1. open excel template
       2. goto $kpi_name row
       3. update both average and maximum columns of this row
       4. save and close file
    '''
    for kpi,values in daily_data.iteritems():
        print kpi, values
    pass

if __name__ == "__main__":
    daily_report = "StarOSDailyReport_2019-01-27.xlsx"
    kpi_daily_data = {} #kpi: (average, maximum)
    for kpi_name, kpi_info in kpi_data.iteritems():
        for kpi,column_name in kpi_info.iteritems():
            print kpi," : ", column_name
            average, maximum = get_kpi_data(daily_report, kpi, column_name)
            kpi_daily_data[kpi] = (average, maximum)
    write_to_excel_template(kpi_daily_data)
