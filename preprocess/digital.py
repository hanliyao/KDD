from preprocess import dataRead
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

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
    features = data[num_features].astype(float)
    ## 最大最小化特征
    scaler = MinMaxScaler()
    features_scaled = pd.DataFrame(scaler.fit_transform(features))
    return features_scaled


def f(x):
    return {
        'smurf.': 0,
        'normal.': 1,
        'neptune.': 2,
        'snmpgetattack.': 3,
        'mailbomb.': 4,
        'guess_passwd.': 5,
        'snmpguess.': 6,
        'satan.': 7,
        'warezmaster.': 8,
        'back.': 9,
        'mscan.': 10,
        'apache2.': 11,
        'processtable.': 12,
        'saint.': 13,
        'portsweep.': 14,
        'ipsweep.': 15,
        'httptunnel.': 16,
        'pod.': 17,
        'nmap.': 18,
        'buffer_overflow.': 19,
        'multihop.': 20,
        'sendmail.': 21,
        'named.': 22,
        'ps.': 23,
        'rootkit.': 24,
        'xterm.': 25,
        'teardrop.': 26,
        'land.': 27,
        'xlock.': 28,
        'xsnoop.': 29,
        'ftp_write.': 30,
        'perl.': 31,
        'sqlattack.': 32,
        'phf.': 33,
        'udpstorm.': 34,
        'loadmodule.': 35,
        'worm.': 36,
        'imap.': 37,
    }.get(x, -1)


def ground_truth(data):
    """
    :param data: 
    :return: 
    """
    truth = []
    if 'types' in data.columns:
        for value in data['types']:
            truth.append(f(value))

    return truth


if __name__ == "__main__":
    data = dataRead.corrected()
    print(ground_truth(data))
