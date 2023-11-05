import glob
import os
import pickle

import header

class Msg:
    def __init__(self, expid):
        #TODO: read list of input frames from file, example: './data/compressed/compress_adv_2740/*'
        #self.fptemplate = fptemplate #'./data/compressed/compress_adv_2740/*'
        #self.fp_list = glob.glob(fptemplate)
        #self.dat_dict  = {fp:open(fp, 'rb').read() for fp in self.fp_list}
        
        self.fparse                 = FILEPARSER()
        self.dat_dict, self.fp_list = self.fparse.return_dat(expid)
        self.expid_dict             = self.fparse.return_expid_dict()
        self.byteIndexList          = self.initializeByteIndex()
        
    def initializeByteIndex(self):
        #TODO: store byteindex of all message for future use
        result = []
        idx = 0
        for fp in self.fp_list:
            datitem = self.dat_dict[fp]
            result.append(idx)
            idx = idx + len(datitem)
        return result
    
    def getMsgIndex(self, byteIndex):
        #TODO: return msgIndex from byteIndex
        if len(self.byteIndexList) <= 1:
            return -1
        if byteIndex == self.byteIndexList[0]:
            return byteIndex
        for i in range(1, len(self.fp_list)):
            len1, len2 = self.byteIndexList[i-1], self.byteIndexList[i]
            if len1 < byteIndex and byteIndex < len2:
                return len1
        return len2
        
    def __getitem__(self, idx):
        fp = self.fp_list[idx]
        return fp, self.dat_dict[fp]

    def __len__(self):
        return len(self.dat_dict)

    def getDatList(self):
        return [self.dat_dict[fp] for fp in self.fp_list]
    
class FILEPARSER:
    #TODO: read file and parse data, and generate simulate dat dict
    DUMMY_FPNAME = 'dummyfp'#key of output datdict is dummy filepath, so here is dummy
    def __init__(self):
        self.fptemplate = header.INPUT_FILETEMPLATE#'./data/compressed_file_size/*'
        self.exp_dict = {}#key:value <==> expid:[packet_size]
        self.expid_dict = {}#key:value <===> expid:filename
        
        #initialize data
        self.parse_files()
        
    def parse_expid_from_fname(self, fp):
        fbase = os.path.basename(fp)
        fbasename, fbaseext = os.path.splitext(fbase)
        return fbasename
        
    def parse_file(self, fp):
        dat = open(fp, 'r').read().split('\n')[3:-1]
        dat = [int(float(item)) for item in dat]
        return dat
    
    def parse_files(self):
        fp_list = glob.glob(self.fptemplate)
        for expid,fp in enumerate(fp_list):
            fbasename = self.parse_expid_from_fname(fp)
            self.exp_dict[expid] = self.parse_file(fp)
            self.expid_dict[expid] = fbasename
    
    #INTERFACE FUNCTION
    def return_dat(self, expid):
        #TODO: simulate packet size data structure
        #   OUTPUT1: DICT: key:value <==> expid:msg# msg is [byte], len(msg) == msgsize 
        #   OUTPUT2: FP_LIST, list of dummyname, each according to a line in the log file
        msgsize_list = self.exp_dict[expid]
        dat_dict = {}
        fp_list  = []
        for msgidx, msgsize in enumerate(msgsize_list):
            fp = f"{self.DUMMY_FPNAME}-{msgidx}"
            fp_list.append(fp)
            dat_dict[fp] = bytearray(msgsize)
        return dat_dict, fp_list
    
    def return_fplist(self, expid):
        return 
    
    def return_expid_dict(self):
        return self.expid_dict
    