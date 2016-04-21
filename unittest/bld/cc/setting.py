#!/usr/bin/python
import sys
import os
import commands

temp_path = './temp/'
temp_data_path = './temp/data/'
temp_info_path = './temp/info/'
temp_html_path = './temp/html/'
temp_xml_path = './temp/xml/'

wme_path = '../../../'
mediaengine_path = '../../../mediaengine/'
wbxtrace_path = '../../../mediaengine/wbxtrace/objs/'
unittest_distribution = '../../../unittest/distribution'

#################################################################################################################


module_list = [
	{"module_name":"util", 	"path":"../../../mediaengine/util", 		'src_path_list':[], 'gcno_path_list':[], 'gcda_path_list':[]},
	{"module_name":"tp", 	"path":"../../../mediaengine/transmission", 'src_path_list':[], 'gcno_path_list':[], 'gcda_path_list':[]},
	{"module_name":"wqos", 	"path":"../../../mediaengine/wqos", 		'src_path_list':[], 'gcno_path_list':[], 'gcda_path_list':[]},
	{"module_name":"wrtp", 	"path":"../../../mediaengine/wrtp", 		'src_path_list':[], 'gcno_path_list':[], 'gcda_path_list':[]},
	{"module_name":"wme", 	"path":"../../../mediaengine/wme", 			'src_path_list':[], 'gcno_path_list':[], 'gcda_path_list':[]},
	{"module_name":"shark", 	"path":"../../../mediaengine/shark", 	'src_path_list':[], 'gcno_path_list':[], 'gcda_path_list':[]},
	{"module_name":"dolphin", 	"path":"../../../mediaengine/dolphin", 	'src_path_list':[], 'gcno_path_list':[], 'gcda_path_list':[]},
]

#################################################################################################################
#run_mode = sim|dev, build_mode = debug|release
def init_ios_setting(run_mode, build_mode):
    #mediasession = {'module_name':'mediasession', 'src_path_list':[], 'gcno_path_list':[], 'gcda_path_list':[], 'path':"../../../mediasession"}
    #module_list.append(mediasession) 
    print 'init_ios_setting %s %s' %(run_mode, build_mode)
    if run_mode == 'dev':
        #print 'IOS code coverage do not support device now'
        #sys.exit(-1)
        platformString = 'iphoneos'
        archString = 'armv7s/'
    else:
        platformString = 'iphonesimulator'
        archString = 'i386/'
            
    if build_mode == 'debug':
        #print 'IOS code coverage do not support debug mode now'
        #sys.exit(-2)
        configString = 'Debug'
    else:
        configString = 'Release'    
    [util, tp, wqos, wrtp, wme, shark, dolphin] = module_list
    #[util, tp, wqos, wrtp, wme, shark, dolphin, _] = module_list
    #############################################################################################################
    util['src_path_list'].append('mediaengine/util/src/')
    util['gcno_path_list'].append('mediaengine/util/objs/ios/util_ios.build/'+configString+'-'+platformString+'/util_ios.build/Objects-normal/'+archString)
    util['gcda_path_list'].append('mediaengine/util/objs/ios/util_ios.build/'+configString+'-'+platformString+'/util_ios.build/Objects-normal/'+archString)


    tp['src_path_list'].append('mediaengine/tp/src/')
    tp['gcno_path_list'].append('mediaengine/tp/objs/ios/tp_ios.build/'+configString+'-'+platformString+'/tp_ios.build/Objects-normal/'+archString)
    tp['gcda_path_list'].append('mediaengine/tp/objs/ios/tp_ios.build/'+configString+'-'+platformString+'/tp_ios.build/Objects-normal/'+archString)

    wqos['src_path_list'].append('mediaengine/wqos/src/')
    wqos['gcno_path_list'].append('mediaengine/wqos/objs/ios/wqos_ios.build/'+configString+'-'+platformString+'/wqos_ios.build/Objects-normal/'+archString)
    wqos['gcda_path_list'].append('mediaengine/wqos/objs/ios/wqos_ios.build/'+configString+'-'+platformString+'/wqos_ios.build/Objects-normal/'+archString)

    wrtp['src_path_list'].append('mediaengine/transmission/src/')
    wrtp['gcno_path_list'].append('mediaengine/transmission/objs/ios/wrtp_ios.build/'+configString+'-'+platformString+'/wrtp_ios.build/Objects-normal/'+archString)
    wrtp['gcda_path_list'].append('mediaengine/transmission/objs/ios/wrtp_ios.build/'+configString+'-'+platformString+'/wrtp_ios.build/Objects-normal/'+archString)

    ##########################################################################################################
    #wseclient
    shark['src_path_list'].append('mediaengine/shark/src/client/SvcClientEngine')
    shark['gcno_path_list'].append('mediaengine/objs/wseclient.build/'+configString+'-'+platformString+'/wseclient.build/Objects-normal/'+archString)
    shark['gcda_path_list'].append('mediaengine/objs/wseclient.build/'+configString+'-'+platformString+'/wseclient.build/Objects-normal/'+archString)

    #wsejlcore
    shark['src_path_list'].append('mediaengine/shark/src/jlcore/')
    shark['gcno_path_list'].append('mediaengine/objs/wseclient.build/'+configString+'-'+platformString+'/wseclient.build/Objects-normal/'+archString)
    shark['gcda_path_list'].append('mediaengine/objs/wseclient.build/'+configString+'-'+platformString+'/wseclient.build/Objects-normal/'+archString)

    #wsecommon
    shark['src_path_list'].append('mediaengine/shark/src/common/')
    shark['gcno_path_list'].append('mediaengine/objs/wseclient.build/'+configString+'-'+platformString+'/wseclient.build/Objects-normal/'+archString)
    shark['gcda_path_list'].append('mediaengine/objs/wseclient.build/'+configString+'-'+platformString+'/wseclient.build/Objects-normal/'+archString)

    #wsertp
    shark['src_path_list'].append('mediaengine/shark/src/rtp/')
    shark['gcno_path_list'].append('mediaengine/objs/wsertp.build/'+configString+'-'+platformString+'/wsertp.build/Objects-normal/'+archString)
    shark['gcda_path_list'].append('mediaengine/objs/wseclient.build/'+configString+'-'+platformString+'/wseclient.build/Objects-normal/'+archString)

    ##########################################################################################################
    #wme_client
    wme['src_path_list'].append('mediaengine/wme/src/client/')
    wme['gcno_path_list'].append('mediaengine/objs/wmeclient.build/'+configString+'-'+platformString+'/wmeclient.build/Objects-normal/'+archString)
    wme['gcda_path_list'].append('mediaengine/objs/wmeclient.build/'+configString+'-'+platformString+'/wmeclient.build/Objects-normal/'+archString)

    #wme_util
    wme['src_path_list'].append('mediaengine/wme/src/common/')
    wme['gcno_path_list'].append('mediaengine/objs/wmeclient.build/'+configString+'-'+platformString+'/wmeclient.build/Objects-normal/'+archString)
    wme['gcda_path_list'].append('mediaengine/objs/wmeclient.build/'+configString+'-'+platformString+'/wmeclient.build/Objects-normal/'+archString)

    #############################################################################################################
    #dolphin_aagc
    dolphin['src_path_list'].append('mediaengine/dolphin/src/cochelea/aagc/wbx_aagc/src/')
    dolphin['gcno_path_list'].append('mediaengine/dolphin/src/cochelea/libs/intermedia/wbx_aagc.build/'+configString+'-'+platformString+'/wbx_aagc.build/Objects-normal/'+archString)
    dolphin['gcda_path_list'].append('mediaengine/dolphin/src/cochelea/libs/intermedia/wbx_aagc.build/'+configString+'-'+platformString+'/wbx_aagc.build/Objects-normal/'+archString)

    #dolphin_cng
    dolphin['src_path_list'].append('mediaengine/dolphin/src/cochelea/cng/src/')
    dolphin['gcno_path_list'].append('mediaengine/dolphin/src/cochelea/libs/intermedia/wbx_cng.build/'+configString+'-'+platformString+'/wbx_cng.build/Objects-normal/'+archString)
    dolphin['gcda_path_list'].append('mediaengine/dolphin/src/cochelea/libs/intermedia/wbx_cng.build/'+configString+'-'+platformString+'/wbx_cng.build/Objects-normal/'+archString)

    #dolphin_dagc
    dolphin['src_path_list'].append('mediaengine/dolphin/src/cochelea/dagc/WebEx_DAGC_Client_16k/src/')
    dolphin['gcno_path_list'].append('mediaengine/dolphin/src/cochelea/libs/intermedia/wbx_dagc.build/'+configString+'-'+platformString+'/wbx_dagc.build/Objects-normal/'+archString)
    dolphin['gcda_path_list'].append('mediaengine/dolphin/src/cochelea/libs/intermedia/wbx_dagc.build/'+configString+'-'+platformString+'/wbx_dagc.build/Objects-normal/'+archString)

    #dolphin_ns
    dolphin['src_path_list'].append('mediaengine/dolphin/src/cochelea/ns/src/')
    dolphin['gcno_path_list'].append('mediaengine/dolphin/src/cochelea/libs/intermedia/wbx_ns.build/'+configString+'-'+platformString+'/wbx_ns.build/Objects-normal/'+archString)
    dolphin['gcda_path_list'].append('mediaengine/dolphin/src/cochelea/libs/intermedia/wbx_ns.build/'+configString+'-'+platformString+'/wbx_ns.build/Objects-normal/'+archString)

    #dolphin_plc
    dolphin['src_path_list'].append('mediaengine/dolphin/src/cochelea/plc/wbx_plc/src/')
    dolphin['gcno_path_list'].append('mediaengine/dolphin/src/cochelea/libs/intermedia/wbx_plc.build/'+configString+'-'+platformString+'/wbx_plc.build/Objects-normal/'+archString)
    dolphin['gcda_path_list'].append('mediaengine/dolphin/src/cochelea/libs/intermedia/wbx_plc.build/'+configString+'-'+platformString+'/wbx_plc.build/Objects-normal/'+archString)

    #dolphin_resample
    dolphin['src_path_list'].append('mediaengine/dolphin/src/cochelea/resample/src/')
    dolphin['gcno_path_list'].append('mediaengine/dolphin/src/cochelea/libs/intermedia/wbx_resample.build/'+configString+'-'+platformString+'/wbx_resample.build/Objects-normal/'+archString)
    dolphin['gcda_path_list'].append('mediaengine/dolphin/src/cochelea/libs/intermedia/wbx_resample.build/'+configString+'-'+platformString+'/wbx_resample.build/Objects-normal/'+archString)

    #dolphin_sa
    dolphin['src_path_list'].append('mediaengine/dolphin/src/cochelea/sa/wbx_signalanalysis/src/')
    dolphin['gcno_path_list'].append('mediaengine/dolphin/src/cochelea/libs/intermedia/wbx_sa.build/'+configString+'-'+platformString+'/wbx_sa.build/Objects-normal/'+archString)
    dolphin['gcda_path_list'].append('mediaengine/dolphin/src/cochelea/libs/intermedia/wbx_sa.build/'+configString+'-'+platformString+'/wbx_sa.build/Objects-normal/'+archString)

    #dolphin_tsm
    dolphin['src_path_list'].append('mediaengine/dolphin/src/cochelea/tsm/')
    dolphin['gcno_path_list'].append('mediaengine/dolphin/src/cochelea/libs/intermedia/wbx_tsm.build/'+configString+'-'+platformString+'/wbx_tsm.build/Objects-normal/'+archString)
    dolphin['gcda_path_list'].append('mediaengine/dolphin/src/cochelea/libs/intermedia/wbx_tsm.build/'+configString+'-'+platformString+'/wbx_tsm.build/Objects-normal/'+archString)

    #dolphin_vad
    dolphin['src_path_list'].append('mediaengine/dolphin/src/cochelea/vad/webexvadver1/src/')
    dolphin['gcno_path_list'].append('mediaengine/dolphin/src/cochelea/libs/intermedia/wbx_vad.build/'+configString+'-'+platformString+'/wbx_vad.build/Objects-normal/'+archString)
    dolphin['gcda_path_list'].append('mediaengine/dolphin/src/cochelea/libs/intermedia/wbx_vad.build/'+configString+'-'+platformString+'/wbx_vad.build/Objects-normal/'+archString)

    #dolphin_aecm
    dolphin['src_path_list'].append('mediaengine/dolphin/src/cochelea/aecm/src/')
    dolphin['gcno_path_list'].append('mediaengine/dolphin/src/cochelea/libs/intermedia/wbx_aecm.build/'+configString+'-'+platformString+'/wbx_aecm.build/Objects-normal/'+archString)
    dolphin['gcda_path_list'].append('mediaengine/dolphin/src/cochelea/libs/intermedia/wbx_aecm.build/'+configString+'-'+platformString+'/wbx_aecm.build/Objects-normal/'+archString)

    #dolphin_aqe
    dolphin['src_path_list'].append('mediaengine/dolphin/src/AudioEngine/src/')
    dolphin['gcno_path_list'].append('mediaengine/objs/wbxaudioengine.build/aqe/'+configString+'-'+platformString+'/wbxaudioengine.build/Objects-normal/'+archString)
    dolphin['gcda_path_list'].append('mediaengine/objs/wbxaudioengine.build/aqe/'+configString+'-'+platformString+'/wbxaudioengine.build/Objects-normal/'+archString)

    #dolphin_capture
    dolphin['src_path_list'].append('mediaengine/dolphin/src/AudioEngine/src/capture/')
    dolphin['gcno_path_list'].append('mediaengine/objs/wbxaudioengine.build/'+configString+'-'+platformString+'/wbxaudioengine.build/Objects-normal/'+archString)
    dolphin['gcda_path_list'].append('mediaengine/objs/wbxaudioengine.build/'+configString+'-'+platformString+'/wbxaudioengine.build/Objects-normal/'+archString)

    #dolphin_common
    dolphin['src_path_list'].append('mediaengine/dolphin/src/AudioEngine/src/common/')
    dolphin['gcno_path_list'].append('mediaengine/objs/wbxaudioengine.build/'+configString+'-'+platformString+'/wbxaudioengine.build/Objects-normal/'+archString)
    dolphin['gcda_path_list'].append('mediaengine/objs/wbxaudioengine.build/'+configString+'-'+platformString+'/wbxaudioengine.build/Objects-normal/'+archString)

    #dolphin_datadump
    dolphin['src_path_list'].append('mediaengine/dolphin/src/AudioEngine/src/datadump/')
    dolphin['gcno_path_list'].append('mediaengine/objs/wbxaudioengine.build/'+configString+'-'+platformString+'/wbxaudioengine.build/Objects-normal/'+archString)
    dolphin['gcda_path_list'].append('mediaengine/objs/wbxaudioengine.build/'+configString+'-'+platformString+'/wbxaudioengine.build/Objects-normal/'+archString)

    #dolphin_device
    dolphin['src_path_list'].append('mediaengine/dolphin/src/AudioEngine/src/deviceenumerator/')
    dolphin['gcno_path_list'].append('mediaengine/objs/wbxaudioengine.build/'+configString+'-'+platformString+'/wbxaudioengine.build/Objects-normal/'+archString)
    dolphin['gcda_path_list'].append('mediaengine/objs/wbxaudioengine.build/'+configString+'-'+platformString+'/wbxaudioengine.build/Objects-normal/'+archString)

    #dolphin_framework
    dolphin['src_path_list'].append('mediaengine/dolphin/src/AudioEngine/src/framework/')
    dolphin['gcno_path_list'].append('mediaengine/objs/wbxaudioengine.build/'+configString+'-'+platformString+'/wbxaudioengine.build/Objects-normal/'+archString)
    dolphin['gcda_path_list'].append('mediaengine/objs/wbxaudioengine.build/'+configString+'-'+platformString+'/wbxaudioengine.build/Objects-normal/'+archString)

    #dolphin_playback
    dolphin['src_path_list'].append('mediaengine/dolphin/src/AudioEngine/src/playback/')
    dolphin['gcno_path_list'].append('mediaengine/objs/wbxaudioengine.build/'+configString+'-'+platformString+'/wbxaudioengine.build/Objects-normal/'+archString)
    dolphin['gcda_path_list'].append('mediaengine/objs/wbxaudioengine.build/'+configString+'-'+platformString+'/wbxaudioengine.build/Objects-normal/'+archString)


    ##
    #mediasession
    #mediasession['src_path_list'].append('mediasession/src/')
    #mediasession['gcno_path_list'].append('mediasession/bld/objs/ios/MediaSession.build/'+configString+'-'+platformString+'/MediaSession.build/Objects-normal/'+archString)
    #mediasession['gcda_path_list'].append('mediasession/bld/objs/ios/MediaSession.build/'+configString+'-'+platformString+'/MediaSession.build/Objects-normal/'+archString)


    #############################################################################################################
    for i in range(len(module_list)):
        for j in range(len(module_list[i]['src_path_list'])):
            module_list[i]['src_path_list'][j] = wme_path + module_list[i]['src_path_list'][j]
            module_list[i]['gcno_path_list'][j] = wme_path + module_list[i]['gcno_path_list'][j]
            if run_mode == 'dev':
                module_list[i]['gcda_path_list'][j] = './gcdaFile/' + module_list[i]['gcda_path_list'][j]
            else:
                module_list[i]['gcda_path_list'][j] = wme_path + module_list[i]['gcda_path_list'][j]

    #############################################################################################################


#run_mode = sim|dev, build_mode = debug|release
def init_android_setting(run_mode, build_mode):
    print 'init_android_setting %s %s' %(run_mode, build_mode)
    if run_mode == 'sim':
        print 'IOS code coverage do not support simulator now'
        exit(-1)
    if build_mode == 'debug':
        print 'IOS code coverage do not support debug mode now'
        exit(-2)

    #device_id = commands.getoutput("adb devices | awk 'NR==2{print $1}'")
    #os.system("adb -s %s pull /sdcard/wme_gcov/mediaengine/ ./temp/data/" % (device_id))
    os.system("rm -rf ./temp/data/*")
    device_ids = commands.getoutput("adb devices | awk -F' ' '/\tdevice/{print $1}'")
    for device_id in device_ids.split():
        os.system("adb -s %s pull /sdcard/wme_gcov/mediaengine/ ./temp/data/" % (device_id))
        if os.system("ls ./temp/data/bin") == 0:
            break

    [util, tp, wqos, wrtp, wme, shark, dolphin] = module_list
    #############################################################################################################
    util['src_path_list'].append('util/src/')
    util['gcno_path_list'].append('util/objs/android/local/armeabi-v7a/objs/util/')
    util['gcda_path_list'].append('./temp/data/util/objs/android/local/armeabi-v7a/objs/util/')

    tp['src_path_list'].append('tp/src/')
    tp['gcno_path_list'].append('tp/objs/android/local/armeabi-v7a/objs/tp/')
    tp['gcda_path_list'].append('./temp/data/tp/objs/android/local/armeabi-v7a/objs/tp/')

    wqos['src_path_list'].append('wqos/src/')
    wqos['gcno_path_list'].append('wqos/objs/android/release/local/armeabi-v7a/objs/wqos/')
    wqos['gcda_path_list'].append('./temp/data/wqos/objs/android/release/local/armeabi-v7a/objs/wqos/')

    wrtp['src_path_list'].append('transmission/src/')
    wrtp['gcno_path_list'].append('transmission/objs/android/release/wrtp/local/armeabi-v7a/objs/wrtp/')
    wrtp['gcda_path_list'].append('./temp/data/transmission/objs/android/release/wrtp/local/armeabi-v7a/objs/wrtp/')

    ##########################################################################################################
    #wseclient
    shark['src_path_list'].append('shark/src/client/SvcClientEngine')
    shark['gcno_path_list'].append('bin/objs/wseclient/local/armeabi-v7a/objs/wseclient/__/__/__/__/__/src/client/SvcClientEngine/')
    shark['gcda_path_list'].append('./temp/data/bin/objs/wseclient/local/armeabi-v7a/objs/wseclient/__/__/__/__/__/src/client/SvcClientEngine/')

    #wsejlcore
    shark['src_path_list'].append('shark/src/jlcore/')
    shark['gcno_path_list'].append('bin/objs/wseclient/local/armeabi-v7a/objs/wseclient/__/__/__/__/__/src/jlcore/')
    shark['gcda_path_list'].append('./temp/data/bin/objs/wseclient/local/armeabi-v7a/objs/wseclient/__/__/__/__/__/src/jlcore/')

    #wsecommon
    shark['src_path_list'].append('shark/src/common/')
    shark['gcno_path_list'].append('bin/objs/wseclient/local/armeabi-v7a/objs/wseclient/__/__/__/__/__/src/common/')
    shark['gcda_path_list'].append('./temp/data/bin/objs/wseclient/local/armeabi-v7a/objs/wseclient/__/__/__/__/__/src/common/')

    #wsertp
    shark['src_path_list'].append('shark/src/rtp/')
    shark['gcno_path_list'].append('dolphin/bld/client/Android/obj/local/armeabi-v7a/objs/rtp/__/__/__/__/__/shark/src/rtp/')
    shark['gcda_path_list'].append('./temp/data/dolphin/bld/client/Android/obj/local/armeabi-v7a/objs/rtp/__/__/__/__/__/shark/src/rtp/')

    ##########################################################################################################
    #wme_client
    wme['src_path_list'].append('wme/src/client/')
    wme['gcno_path_list'].append('bin/objs/wmeclient/local/armeabi-v7a/objs/wmeclient/__/__/__/__/src/client/')
    wme['gcda_path_list'].append('./temp/data/bin/objs/wmeclient/local/armeabi-v7a/objs/wmeclient/__/__/__/__/src/client/')

    #wme_util
    wme['src_path_list'].append('wme/src/common/')
    wme['gcno_path_list'].append('/bin/objs/wmeclient/local/armeabi-v7a/objs/wmeclient/__/__/__/__/src/common/')
    wme['gcda_path_list'].append('./temp/data/bin/objs/wmeclient/local/armeabi-v7a/objs/wmeclient/__/__/__/__/src/common/')

    #############################################################################################################
    #dolphin_aagc
    dolphin['src_path_list'].append('dolphin/src/cochelea/aagc/wbx_aagc/src/')
    dolphin['gcno_path_list'].append('dolphin/src/cochelea/cwcochlea_bld/Android/obj/local/armeabi-v7a/objs/AAGC/__/__/__/aagc/wbx_aagc/src/')
    dolphin['gcda_path_list'].append('./temp/data/dolphin/src/cochelea/cwcochlea_bld/Android/obj/local/armeabi-v7a/objs/AAGC/__/__/__/aagc/wbx_aagc/src/')

    #dolphin_cng
    dolphin['src_path_list'].append('dolphin/src/cochelea/cng/src/')
    dolphin['gcno_path_list'].append('dolphin/src/cochelea/cwcochlea_bld/Android/obj/local/armeabi-v7a/objs/cng/__/__/__/cng/src/')
    dolphin['gcda_path_list'].append('./temp/data/dolphin/src/cochelea/cwcochlea_bld/Android/obj/local/armeabi-v7a/objs/cng/__/__/__/cng/src/')

    #dolphin_dagc
    dolphin['src_path_list'].append('dolphin/src/cochelea/dagc/WebEx_DAGC_Client_16k/src/')
    dolphin['gcno_path_list'].append('dolphin/src/cochelea/cwcochlea_bld/Android/obj/local/armeabi-v7a/objs/DAGC/__/__/__/dagc/WebEx_DAGC_Client_16k/src/')
    dolphin['gcda_path_list'].append('./temp/data/dolphin/src/cochelea/cwcochlea_bld/Android/obj/local/armeabi-v7a/objs/DAGC/__/__/__/dagc/WebEx_DAGC_Client_16k/src/')

    #dolphin_ns
    dolphin['src_path_list'].append('dolphin/src/cochelea/ns/src/')
    dolphin['gcno_path_list'].append('dolphin/src/cochelea/cwcochlea_bld/Android/obj/local/armeabi-v7a/objs/ns/__/__/__/ns/src/')
    dolphin['gcda_path_list'].append('./temp/data/dolphin/src/cochelea/cwcochlea_bld/Android/obj/local/armeabi-v7a/objs/ns/__/__/__/ns/src/')

    #dolphin_plc
    dolphin['src_path_list'].append('dolphin/src/cochelea/plc/wbx_plc/src/')
    dolphin['gcno_path_list'].append('dolphin/src/cochelea/cwcochlea_bld/Android/obj/local/armeabi-v7a/objs/plc/__/__/__/plc/wbx_plc/src/')
    dolphin['gcda_path_list'].append('./temp/data/dolphin/src/cochelea/cwcochlea_bld/Android/obj/local/armeabi-v7a/objs/plc/__/__/__/plc/wbx_plc/src/')

    #dolphin_resample
    dolphin['src_path_list'].append('dolphin/src/cochelea/resample/src/')
    dolphin['gcno_path_list'].append('dolphin/src/cochelea/cwcochlea_bld/Android/obj/local/armeabi-v7a/objs/resample/__/__/__/resample/src/')
    dolphin['gcda_path_list'].append('./temp/data/dolphin/src/cochelea/cwcochlea_bld/Android/obj/local/armeabi-v7a/objs/resample/__/__/__/resample/src/')

    #dolphin_sa
    dolphin['src_path_list'].append('dolphin/src/cochelea/sa/wbx_signalanalysis/src/')
    dolphin['gcno_path_list'].append('dolphin/src/cochelea/cwcochlea_bld/Android/obj/local/armeabi-v7a/objs/sa/__/__/__/sa/wbx_signalanalysis/src/')
    dolphin['gcda_path_list'].append('./temp/data/dolphin/src/cochelea/cwcochlea_bld/Android/obj/local/armeabi-v7a/objs/sa/__/__/__/sa/wbx_signalanalysis/src/')

    #dolphin_tsm
    dolphin['src_path_list'].append('dolphin/src/cochelea/tsm/')
    dolphin['gcno_path_list'].append('dolphin/src/cochelea/cwcochlea_bld/Android/obj/local/armeabi-v7a/objs/tsm/__/__/__/tsm/')
    dolphin['gcda_path_list'].append('./temp/data/dolphin/src/cochelea/cwcochlea_bld/Android/obj/local/armeabi-v7a/objs/tsm/__/__/__/tsm/')

    #dolphin_vad
    dolphin['src_path_list'].append('dolphin/src/cochelea/vad/webexvadver1/src/')
    dolphin['gcno_path_list'].append('dolphin/src/cochelea/cwcochlea_bld/Android/obj/local/armeabi-v7a/objs/vad/__/__/__/vad/webexvadver1/src/')
    dolphin['gcda_path_list'].append('./temp/data/dolphin/src/cochelea/cwcochlea_bld/Android/obj/local/armeabi-v7a/objs/vad/__/__/__/vad/webexvadver1/src/')

    #dolphin_aecm
    dolphin['src_path_list'].append('dolphin/src/cochelea/aecm/src/')
    dolphin['gcno_path_list'].append('dolphin/src/cochelea/cwcochlea_bld/Android/obj/local/armeabi-v7a/objs/AEC/__/__/__/aecm/src/')
    dolphin['gcda_path_list'].append('./temp/data/dolphin/src/cochelea/cwcochlea_bld/Android/obj/local/armeabi-v7a/objs/AEC/__/__/__/aecm/src/')

    #dolphin_aqe
    dolphin['src_path_list'].append('dolphin/src/AudioEngine/src/')
    dolphin['gcno_path_list'].append('dolphin/bld/client/Android/obj/local/armeabi-v7a/objs/aqe/__/__/__/__/__/dolphin/src/AudioEngine/src/aqe/')
    dolphin['gcda_path_list'].append('./temp/data/dolphin/bld/client/Android/obj/local/armeabi-v7a/objs/aqe/__/__/__/__/__/dolphin/src/AudioEngine/src/aqe/')

    #dolphin_capture
    dolphin['src_path_list'].append('dolphin/src/AudioEngine/src/capture/')
    dolphin['gcno_path_list'].append('dolphin/bld/client/Android/obj/local/armeabi-v7a/objs/capture/__/__/__/__/__/dolphin/src/AudioEngine/src/capture/android/')
    dolphin['gcda_path_list'].append('./temp/data/dolphin/bld/client/Android/obj/local/armeabi-v7a/objs/capture/__/__/__/__/__/dolphin/src/AudioEngine/src/capture/android/')

    #dolphin_common
    dolphin['src_path_list'].append('dolphin/src/AudioEngine/src/common/')
    dolphin['gcno_path_list'].append('dolphin/bld/client/Android/obj/local/armeabi-v7a/objs/common/__/__/__/__/__/dolphin/src/AudioEngine/src/common/')
    dolphin['gcda_path_list'].append('./temp/data/dolphin/bld/client/Android/obj/local/armeabi-v7a/objs/common/__/__/__/__/__/dolphin/src/AudioEngine/src/common/')

    #dolphin_datadump
    dolphin['src_path_list'].append('dolphin/src/AudioEngine/src/datadump/')
    dolphin['gcno_path_list'].append('dolphin/bld/client/Android/obj/local/armeabi-v7a/objs/common/__/__/__/__/__/dolphin/src/AudioEngine/src/datadump/')
    dolphin['gcda_path_list'].append('./temp/data/dolphin/bld/client/Android/obj/local/armeabi-v7a/objs/common/__/__/__/__/__/dolphin/src/AudioEngine/src/datadump/')

    #dolphin_device
    dolphin['src_path_list'].append('dolphin/src/AudioEngine/src/deviceenumerator/')
    dolphin['gcno_path_list'].append('dolphin/bld/client/Android/obj/local/armeabi-v7a/objs/deviceenumerator/__/__/__/__/__/dolphin/src/AudioEngine/src/deviceenumerator/')
    dolphin['gcda_path_list'].append('./temp/data/dolphin/bld/client/Android/obj/local/armeabi-v7a/objs/deviceenumerator/__/__/__/__/__/dolphin/src/AudioEngine/src/deviceenumerator/')

    #dolphin_framework
    dolphin['src_path_list'].append('dolphin/src/AudioEngine/src/framework/')
    dolphin['gcno_path_list'].append('dolphin/bld/client/Android/obj/local/armeabi-v7a/objs/framework/__/__/__/__/__/dolphin/src/AudioEngine/src/framework/')
    dolphin['gcda_path_list'].append('./temp/data/dolphin/bld/client/Android/obj/local/armeabi-v7a/objs/framework/__/__/__/__/__/dolphin/src/AudioEngine/src/framework/')

    #dolphin_playback
    dolphin['src_path_list'].append('dolphin/src/AudioEngine/src/playback/')
    dolphin['gcno_path_list'].append('dolphin/bld/client/Android/obj/local/armeabi-v7a/objs/playback/__/__/__/__/__/dolphin/src/AudioEngine/src/playback/android/')
    dolphin['gcda_path_list'].append('./temp/data/dolphin/bld/client/Android/obj/local/armeabi-v7a/objs/playback/__/__/__/__/__/dolphin/src/AudioEngine/src/playback/android/')

    #############################################################################################################
    for i in range(len(module_list)):
        for j in range(len(module_list[i]['src_path_list'])):
            module_list[i]['src_path_list'][j] = mediaengine_path + module_list[i]['src_path_list'][j]
            module_list[i]['gcno_path_list'][j] = mediaengine_path + module_list[i]['gcno_path_list'][j]

    #############################################################################################################

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 2:
        print "Usage: ./setting [sim|dev] [debug|release]"
        sys.exit()
    run_mode = args[0]
    build_mode = args[1]
    #init_ios_setting(run_mode, build_mode);