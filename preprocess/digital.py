from preprocess import dataRead

def info(data):
    """
    获取当前数据集的基本信息
    :param data: 
    :return: 
    """
    return data['types'].value_counts()

## symbolic
def protocol_type(data,symbolic):
    """
    protocol_type: icmp tcp udp
    service: ecr_i  private  http  smtp  pop_3  domain_u  ftp_data  other  telnet  ftp  eco_i  imap4  finger  sunrpc  auth  time  ntp_u  echo  domain  link  bgp  netstat  remote_job  gopher  netbios_ns  urp_i  ctf  uucp  iso_tsap  nntp  exec  login  pop_2  name  discard  http_443  kshell  ldap  nnsp  netbios_dgm  rje  courier  printer  systat  mtp  uucp_path  ssh  Z39_50  efs  sql_net  vmnet  shell  netbios_ssn  daytime  whois  supdup  klogin  csnet_ns  hostnames  IRC  pm_dump  X11  tim_i  icmp  tftp_u
    flag: SF  REJ  S0  RSTO  RSTR  S3  SH  S1  S2  OTH  RSTOS0
    land: 0  1
    logged_in: 0  1
    is_host_login: 0  1
    is_guest_login: 0  1
    :param data: 
    :return: 
    """
    return data[symbolic].value_counts()


## 规范化连续特征
def contious_features(data):
    """
    
    :param data: 
    :return: 
    """
    num_features = [
        "duration", "src_bytes",
        "dst_bytes", "land", "wrong_fragment", "urgent", "hot", "num_failed_logins",
        "logged_in", "num_compromised", "root_shell", "su_attempted", "num_root",
        "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds",
        "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate",
        "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate",
        "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
        "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
        "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate",
        "dst_host_rerror_rate", "dst_host_srv_rerror_rate"
    ]
    return data[num_features].astype(float)


if __name__ == "__main__":
    data = dataRead.corrected()
    print(protocol_type(data))