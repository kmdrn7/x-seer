def formatRawData(raw):
    return {
        'Flow ID': raw['flow_id'],
        'Src IP': raw['src_ip'],
        'Src Port': raw['src_port'],
        'Dst IP': raw['dst_ip'],
        'Dst Port': raw['dst_port'],
        'Protocol': raw['protocol'],
        'Timestamp': raw['timestamp'],
        'Flow Duration': raw['extractFeature']['flow_duration'],
        'Total Fwd Packet': raw['extractFeature']['totalPacketFeature']['forward'],
        'Total Bwd packets': raw['extractFeature']['totalPacketFeature']['backward'],
        'Total Length of Fwd Packet': raw['extractFeature']['totalPacketFeature']['length_of_forward'],
        'Total Length of Bwd Packet': raw['extractFeature']['totalPacketFeature']['length_of_backward'],
        'Fwd Packet Length Max': raw['extractFeature']['fwd_packet_length']['max'],
        'Fwd Packet Length Min': raw['extractFeature']['fwd_packet_length']['min'],
        'Fwd Packet Length Mean': raw['extractFeature']['fwd_packet_length']['mean'],
        'Fwd Packet Length Std': raw['extractFeature']['fwd_packet_length']['std'],
        'Bwd Packet Length Max': raw['extractFeature']['bwd_packet_length']['max'],
        'Bwd Packet Length Min': raw['extractFeature']['bwd_packet_length']['min'],
        'Bwd Packet Length Mean': raw['extractFeature']['bwd_packet_length']['mean'],
        'Bwd Packet Length Std': raw['extractFeature']['bwd_packet_length']['std'],
        'Flow Bytes/s': raw['extractFeature']['flow_bytes_per_second'],
        'Flow Packets/s': raw['extractFeature']['flow_pkts_per_second'],
        'Flow IAT Mean': raw['extractFeature']['flow_IAT']['mean'],
        'Flow IAT Std': raw['extractFeature']['flow_IAT']['std'],
        'Flow IAT Max': raw['extractFeature']['flow_IAT']['max'],
        'Flow IAT Min': raw['extractFeature']['flow_IAT']['min'],
        'Fwd IAT Total': raw['extractFeature']['fwd_IAT_total'],
        'Fwd IAT Mean': raw['extractFeature']['fwd_IAT']['mean'],
        'Fwd IAT Std': raw['extractFeature']['fwd_IAT']['std'],
        'Fwd IAT Max': raw['extractFeature']['fwd_IAT']['max'],
        'Fwd IAT Min': raw['extractFeature']['fwd_IAT']['min'],
        'Bwd IAT Total': raw['extractFeature']['bwd_IAT_total'],
        'Bwd IAT Mean': raw['extractFeature']['bwd_IAT']['mean'],
        'Bwd IAT Std': raw['extractFeature']['bwd_IAT']['std'],
        'Bwd IAT Max': raw['extractFeature']['bwd_IAT']['max'],
        'Bwd IAT Min': raw['extractFeature']['bwd_IAT']['min'],
        'Fwd PSH Flags': raw['extractFeature']['fwd_PSH_flags'],
        'Bwd PSH Flags': raw['extractFeature']['bwd_PSH_flags'],
        'Fwd URG Flags': raw['extractFeature']['fwd_URG_flags'],
        'Bwd URG Flags': raw['extractFeature']['bwd_URG_flags'],
        'Fwd Header Length': raw['extractFeature']['fwd_header_length'],
        'Bwd Header Length': raw['extractFeature']['bwd_header_length'],
        'Fwd Packets/s': raw['extractFeature']['fwd_packets_per_second'],
        'Bwd Packets/s': raw['extractFeature']['bwd_packets_per_second'],
        'Packet Length Min': raw['extractFeature']['packet_lenght']['min'],
        'Packet Length Max': raw['extractFeature']['packet_lenght']['max'],
        'Packet Length Mean': raw['extractFeature']['packet_lenght']['mean'],
        'Packet Length Std': raw['extractFeature']['packet_lenght']['std'],
        'Packet Length Variance': raw['extractFeature']['packet_length_variance'],
        'FIN Flag Count': raw['extractFeature']['flagCount']['fin'],
        'SYN Flag Count': raw['extractFeature']['flagCount']['syn'],
        'RST Flag Count': raw['extractFeature']['flagCount']['rst'],
        'PSH Flag Count': raw['extractFeature']['flagCount']['psh'],
        'ACK Flag Count': raw['extractFeature']['flagCount']['ack'],
        'URG Flag Count': raw['extractFeature']['flagCount']['ugr'],
        'CWR Flag Count': raw['extractFeature']['flagCount']['cwr'],
        'ECE Flag Count': raw['extractFeature']['flagCount']['ece'],
        'Down/Up Ratio': raw['extractFeature']['download_upload_ratio'],
        'Average Packet Size': raw['extractFeature']['average_packet_size'],
        'Fwd Segment Size Avg': raw['extractFeature']['fwd_segment_size_avg'],
        'Bwd Segment Size Avg': raw['extractFeature']['bwd_segment_size_avg'],
        'Fwd Bytes/Bulk Avg': raw['extractFeature']['fwd_bulk']['bytes_per_bulk'],
        'Fwd Packet/Bulk Avg': raw['extractFeature']['fwd_bulk']['packet_per_bulk'],
        'Fwd Bulk Rate Avg': raw['extractFeature']['fwd_bulk']['bulk_rate'],
        'Bwd Bytes/Bulk Avg': raw['extractFeature']['bwd_bulk']['bytes_per_bulk'],
        'Bwd Packet/Bulk Avg': raw['extractFeature']['bwd_bulk']['packet_per_bulk'],
        'Bwd Bulk Rate Avg': raw['extractFeature']['bwd_bulk']['bulk_rate'],
        'Subflow Fwd Packets': raw['extractFeature']['fwd_subflow']['subflow_packets'],
        'Subflow Fwd Bytes': raw['extractFeature']['fwd_subflow']['subflow_bytes'],
        'Subflow Bwd Packets': raw['extractFeature']['bwd_subflow']['subflow_packets'],
        'Subflow Bwd Bytes': raw['extractFeature']['bwd_subflow']['subflow_bytes'],
        'FWD Init Win Bytes': raw['extractFeature']['fwd_win_bytes'],
        'Bwd Init Win Bytes': raw['extractFeature']['bwd_win_bytes'],
        'Fwd Act Data Pkts': raw['extractFeature']['fwd_act_data_pkts'],
        'Fwd Seg Size Min': raw['extractFeature']['fwd_seg_size_min'],
        'Active Mean': raw['extractFeature']['ActivePacket']['mean'],
        'Active Std': raw['extractFeature']['ActivePacket']['std'],
        'Active Max': raw['extractFeature']['ActivePacket']['max'],
        'Active Min': raw['extractFeature']['ActivePacket']['min'],
        'Idle Mean': raw['extractFeature']['IdlePacket']['mean'],
        'Idle Std': raw['extractFeature']['IdlePacket']['std'],
        'Idle Max': raw['extractFeature']['IdlePacket']['max'],
        'Idle Min': raw['extractFeature']['IdlePacket']['min'],
        'Label': raw['label'],
    }