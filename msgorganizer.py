import glob
import pickle

class Msg:
    def __init__(self, fptemplate):
        #TODO: read list of input frames from file, example: './data/compressed/compress_adv_2740/*'
        self.fptemplate = fptemplate #'./data/compressed/compress_adv_2740/*'
        self.fp_list = glob.glob(fptemplate)
        self.dat_dict  = {fp:open(fp, 'rb').read() for fp in self.fp_list}
        self.byteIndexList = self.initializeByteIndex()
        
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