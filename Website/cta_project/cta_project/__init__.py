from pyramid.config import Configurator
from pyramid.events import subscriber
from pyramid.events import NewRequest
import pymongo
from pymongo import MongoClient
from pyramid.response import Response
from cta_project.resources import Root
import csv
def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    config = Configurator(settings=settings, root_factory=Root)
    config.add_view('cta_project.views.my_view',
                    context='cta_project:resources.Root',
                    renderer='cta_project:templates/mytemplate.pt')
    config.add_static_view('static', 'cta_project:static')
    config.include('pyramid_chameleon')
    config.add_route('csv2' , '/csv2')
    config.add_route('wea_ws', '/wea_ws')
    config.add_view('cta_project.views.csvview', route_name = 'csv2')
    config.add_view('cta_project.views.wea_ws', route_name = 'wea_ws')
    config.add_route('wea_hum', '/wea_hum')
    config.add_view('cta_project.views.wea_hum', route_name = 'wea_hum')
    config.add_route('wea_gust', '/wea_gust')
    config.add_view('cta_project.views.wea_gust', route_name = 'wea_gust')
	
    config.add_route('wea_see', '/wea_see')
    config.add_view('cta_project.views.wea_see', route_name = 'wea_see')
	
    config.add_route('wea_dust', '/wea_dust')
    config.add_view('cta_project.views.wea_dust', route_name = 'wea_dust')	
	
    config.add_route('rec_temp', '/rec_temp')
    config.add_view('cta_project.views.rec_temp', route_name = 'rec_temp')	
	
    config.add_route('camtd_daq', '/camtd_daq')
    config.add_view('cta_project.views.camtd_daq', route_name = 'camtd_daq')
	
    config.add_route('camipr_daq', '/camipr_daq')
    config.add_view('cta_project.views.camipr_daq', route_name = 'camipr_daq')	
	
    config.add_route('camiprerr_daq', '/camiprerr_daq')
    config.add_view('cta_project.views.camiprerr_daq', route_name = 'camiprerr_daq')
	
    config.add_route('calq_cal', '/calq_cal')
    config.add_view('cta_project.views.calq_cal', route_name = 'calq_cal')
	
    config.add_route('calq_int', '/calq_int')
    config.add_view('cta_project.views.calq_int', route_name = 'calq_int')	
	
    config.add_route('calq_sig', '/calq_sig')
    config.add_view('cta_project.views.calq_sig', route_name = 'calq_sig')

    config.add_route('drvzd', '/drvzd')
    config.add_view('cta_project.views.drvzd', route_name = 'drvzd')
	
    config.add_route('drvdev_daq', '/drvdev_daq')
    config.add_view('cta_project.views.drvdev_daq', route_name = 'drvdev_daq')	
	
    config.add_route('camhv_daq', '/camhv_daq')
    config.add_view('cta_project.views.camhv_daq', route_name = 'camhv_daq')	
	
    config.add_route('camdc_daq', '/camdc_daq')
    config.add_view('cta_project.views.camdc_daq', route_name = 'camdc_daq')
	
    config.add_route('camdt_daq', '/camdt_daq')
    config.add_view('cta_project.views.camdt_daq', route_name = 'camdt_daq')	
	
    config.add_route('campd_daq', '/campd_daq')
    config.add_view('cta_project.views.campd_daq', route_name = 'campd_daq')
	
    config.add_route('campixtemp_daq', '/campixtemp_daq')
    config.add_view('cta_project.views.campixtemp_daq', route_name = 'campixtemp_daq')
	
    config.add_route('meanpixtemp_daq', '/meanpixtemp_daq')
    config.add_view('cta_project.views.meanpixtemp_daq', route_name = 'meanpixtemp_daq')	
	
    config.add_route('camclusttemp', '/camclusttemp')
    config.add_view('cta_project.views.camclusttemp', route_name = 'camclusttemp')

    config.add_route('camvcelbias_daq', '/camvcelbias_daq')
    config.add_view('cta_project.views.camvcelbias_daq', route_name = 'camvcelbias_daq')
	
    config.add_route('camlv1temp', '/camlv1temp')
    config.add_view('cta_project.views.camlv1temp', route_name = 'camlv1temp')	
	
    config.add_route('camlv2temp', '/camlv2temp')
    config.add_view('cta_project.views.camlv2temp', route_name = 'camlv2temp')	
	
    config.add_route('camlv1hum', '/camlv1hum')
    config.add_view('cta_project.views.camlv1hum', route_name = 'camlv1hum')
	
    config.add_route('camlv2hum', '/camlv2hum')
    config.add_view('cta_project.views.camlv2hum', route_name = 'camlv2hum')	
	
    config.add_route('camcoolfcptopleft', '/camcoolfcptopleft')
    config.add_view('cta_project.views.camcoolfcptopleft', route_name = 'camcoolfcptopleft')
	
    config.add_route('camcoolfcpbottright', '/camcoolfcpbottright')
    config.add_view('cta_project.views.camcoolfcpbottright', route_name = 'camcoolfcpbottright')
	
    config.add_route('camcoolrcptopleft', '/camcoolrcptopleft')
    config.add_view('cta_project.views.camcoolrcptopleft', route_name = 'camcoolrcptopleft')	
	
    config.add_route('camcoolrcpbottright', '/camcoolrcpbottright')
    config.add_view('cta_project.views.camcoolrcpbottright', route_name = 'camcoolrcpbottright')

    config.add_route('camcoolchasiastopleft', '/camcoolchasiastopleft')
    config.add_view('cta_project.views.camcoolchasiastopleft', route_name = 'camcoolchasiastopleft')
	
    config.add_route('camcoolchasiasbottright', '/camcoolchasiasbottright')
    config.add_view('cta_project.views.camcoolchasiasbottright', route_name = 'camcoolchasiasbottright')	
	
    config.add_route('camcoolchasiasftopleft', '/camcoolchasiasftopleft')
    config.add_view('cta_project.views.camcoolchasiasftopleft', route_name = 'camcoolchasiasftopleft')	
	
    config.add_route('camcoolchasiasfbottright', '/camcoolchasiasfbottright')
    config.add_view('cta_project.views.camcoolchasiasfbottright', route_name = 'camcoolchasiasfbottright')
	
    config.add_route('camcoolrearbottleft', '/camcoolrearbottleft')
    config.add_view('cta_project.views.camcoolrearbottleft', route_name = 'camcoolrearbottleft')	
	
    config.add_route('camcoolreartopleft', '/camcoolreartopleft')
    config.add_view('cta_project.views.camcoolreartopleft', route_name = 'camcoolreartopleft')
	
    config.add_route('camcoolfrontbottright', '/camcoolfrontbottright')
    config.add_view('cta_project.views.camcoolfrontbottright', route_name = 'camcoolfrontbottright')
	
    config.add_route('camcoolfronttopright', '/camcoolfronttopright')
    config.add_view('cta_project.views.camcoolfronttopright', route_name = 'camcoolfronttopright')	
	
    config.add_route('amcerr', '/amcerr')
    config.add_view('cta_project.views.amcerr', route_name = 'amcerr')

    config.add_route('l1t', '/l1t')
    config.add_view('cta_project.views.l1t', route_name = 'l1t')
	
    config.add_route('l2t', '/l2t')
    config.add_view('cta_project.views.l2t', route_name = 'l2t')	
	
    config.add_route('l2t_daq', '/l2t_daq')
    config.add_view('cta_project.views.l2t_daq', route_name = 'l2t_daq')	
	
    config.add_route('sumt_globr', '/sumt_globr')
    config.add_view('cta_project.views.sumt_globr', route_name = 'sumt_globr')
	
    config.add_route('sumt_l3', '/sumt_l3')
    config.add_view('cta_project.views.sumt_l3', route_name = 'sumt_l3')	
	
    config.add_route('sumt_dtw', '/sumt_dtw')
    config.add_view('cta_project.views.sumt_dtw', route_name = 'sumt_dtw')
	
    config.add_route('sumt_cbt1', '/sumt_cbt1')
    config.add_view('cta_project.views.sumt_cbt1', route_name = 'sumt_cbt1')
	
    config.add_route('sumt_cbt2', '/sumt_cbt2')
    config.add_view('cta_project.views.sumt_cbt2', route_name = 'sumt_cbt2')	
	
    config.add_route('sumt_ac', '/sumt_ac')
    config.add_view('cta_project.views.sumt_ac', route_name = 'sumt_ac')
	
    config.add_route('sumt_astrob', '/sumt_astrob')
    config.add_view('cta_project.views.sumt_astrob', route_name = 'sumt_astrob')
	
    config.add_route('cool_crate', '/cool_crate')
    config.add_view('cta_project.views.cool_crate', route_name = 'cool_crate')	
	
    config.add_route('cool_rack', '/cool_rack')
    config.add_view('cta_project.views.cool_rack', route_name = 'cool_rack')	
	
    config.add_route('calbtemp1', '/calbtemp1')
    config.add_view('cta_project.views.calbtemp1', route_name = 'calbtemp1')
	
    config.add_route('calbtemp2', '/calbtemp2')
    config.add_view('cta_project.views.calbtemp2', route_name = 'calbtemp2')	
	
    config.add_route('calbhum', '/calbhum')
    config.add_view('cta_project.views.calbhum', route_name = 'calbhum')
	
    config.add_route('sg_devaz', '/sg_devaz')
    config.add_view('cta_project.views.sg_devaz', route_name = 'sg_devaz')
	
    config.add_route('sg_devzd', '/sg_devzd')
    config.add_view('cta_project.views.sg_devzd', route_name = 'sg_devzd')	
	
    config.add_route('sg_camcx', '/sg_camcx')
    config.add_view('cta_project.views.sg_camcx', route_name = 'sg_camcx')

    config.add_route('sg_camcy', '/sg_camcy')
    config.add_view('cta_project.views.sg_camcy', route_name = 'sg_camcy')
	
    config.add_route('sg_stars', '/sg_stars')
    config.add_view('cta_project.views.sg_stars', route_name = 'sg_stars')	
	
    config.add_route('sg_bright', '/sg_bright')
    config.add_view('cta_project.views.sg_bright', route_name = 'sg_bright')	
	
    config.add_route('wea_temp', '/wea_temp')
    config.add_view('cta_project.views.wea_temp', route_name = 'wea_temp')
	
    config.add_route('pyro_cloud', '/pyro_cloud')
    config.add_view('cta_project.views.pyro_cloud', route_name = 'pyro_cloud')	
	
    config.add_route('pyro_skyt', '/pyro_skyt')
    config.add_view('cta_project.views.pyro_skyt', route_name = 'pyro_skyt')
	
    config.add_route('las_trans3km', '/las_trans3km')
    config.add_view('cta_project.views.las_trans3km', route_name = 'las_trans3km')
	
    config.add_route('las_trans6km', '/las_trans6km')
    config.add_view('cta_project.views.las_trans6km', route_name = 'las_trans6km')	
	
    config.add_route('las_trans9km', '/las_trans9km')
    config.add_view('cta_project.views.las_trans9km', route_name = 'las_trans9km')
	
    config.add_route('las_trans12km', '/las_trans12km')
    config.add_view('cta_project.views.las_trans12km', route_name = 'las_trans12km')
	
    config.add_route('muon_psf', '/muon_psf')
    config.add_view('cta_project.views.muon_psf', route_name = 'muon_psf')	
	
    config.add_route('muon_psfn', '/muon_psfn')
    config.add_view('cta_project.views.muon_psfn', route_name = 'muon_psfn')	
	
    config.add_route('muon_size', '/muon_size')
    config.add_view('cta_project.views.muon_size', route_name = 'muon_size')
	
    config.add_route('sbigpsf_b', '/sbigpsf_b')
    config.add_view('cta_project.views.sbigpsf_b', route_name = 'sbigpsf_b')	
	
    config.add_route('sbigpsf_l', '/sbigpsf_l')
    config.add_view('cta_project.views.sbigpsf_l', route_name = 'sbigpsf_l')
	
    config.add_route('bias_sig', '/bias_sig')
    config.add_view('cta_project.views.bias_sig', route_name = 'bias_sig')	
	
    config.add_route('hitfrac_sig', '/hitfrac_sig')
    config.add_view('cta_project.views.hitfrac_sig', route_name = 'hitfrac_sig')
	
    config.add_route('arrtm_cal', '/arrtm_cal')
    config.add_view('cta_project.views.arrtm_cal', route_name = 'arrtm_cal')	
	
    config.add_route('arrtm_int', '/arrtm_int')
    config.add_view('cta_project.views.arrtm_int', route_name = 'arrtm_int')
	
    config.add_route('arrtm_sig', '/arrtm_sig')
    config.add_view('cta_project.views.arrtm_sig', route_name = 'arrtm_sig')
	
    config.add_route('arrtmrms_cal', '/arrtmrms_cal')
    config.add_view('cta_project.views.arrtmrms_cal', route_name = 'arrtmrms_cal')	
	
    config.add_route('arrtmrms_int', '/arrtmrms_int')
    config.add_view('cta_project.views.arrtmrms_int', route_name = 'arrtmrms_int')
	
    config.add_route('arrtmrms_sig', '/arrtmrms_sig')
    config.add_view('cta_project.views.arrtmrms_sig', route_name = 'arrtmrms_sig')
	
    config.add_route('ped_ped', '/ped_ped')
    config.add_view('cta_project.views.ped_ped', route_name = 'ped_ped')	
	
    config.add_route('ped_int', '/ped_int')
    config.add_view('cta_project.views.ped_int', route_name = 'ped_int')	
	
    config.add_route('npe_int', '/npe_int')
    config.add_view('cta_project.views.npe_int', route_name = 'npe_int')
	
    config.add_route('pedrms_ped', '/pedrms_ped')
    config.add_view('cta_project.views.pedrms_ped', route_name = 'pedrms_ped')	
	
    config.add_route('pedrms_int', '/pedrms_int')
    config.add_view('cta_project.views.pedrms_int', route_name = 'pedrms_int')

    config.add_route('cfact_int', '/cfact_int')
    config.add_view('cta_project.views.cfact_int', route_name = 'cfact_int')
    config.add_route('wea_wsy', '/wea_wsy')	
    config.add_view('cta_project.views.wea_wsy', route_name = 'wea_wsy')
    config.add_route('wea_humy', '/wea_humy')
    config.add_view('cta_project.views.wea_humy', route_name = 'wea_humy')
    config.add_route('wea_gusty', '/wea_gusty')
    config.add_view('cta_project.views.wea_gusty', route_name = 'wea_gusty')
	
    config.add_route('wea_seey', '/wea_seey')
    config.add_view('cta_project.views.wea_seey', route_name = 'wea_seey')
	
    config.add_route('wea_dusty', '/wea_dusty')
    config.add_view('cta_project.views.wea_dusty', route_name = 'wea_dusty')	
	
    config.add_route('rec_tempy', '/rec_tempy')
    config.add_view('cta_project.views.rec_tempy', route_name = 'rec_tempy')	
	
    config.add_route('camtd_daqy', '/camtd_daqy')
    config.add_view('cta_project.views.camtd_daqy', route_name = 'camtd_daqy')
	
    config.add_route('camipr_daqy', '/camipr_daqy')
    config.add_view('cta_project.views.camipr_daqy', route_name = 'camipr_daqy')	
	
    config.add_route('camiprerr_daqy', '/camiprerr_daqy')
    config.add_view('cta_project.views.camiprerr_daqy', route_name = 'camiprerr_daqy')
	
    config.add_route('calq_caly', '/calq_caly')
    config.add_view('cta_project.views.calq_caly', route_name = 'calq_caly')
	
    config.add_route('calq_inty', '/calq_inty')
    config.add_view('cta_project.views.calq_inty', route_name = 'calq_inty')	
	
    config.add_route('calq_sigy', '/calq_sigy')
    config.add_view('cta_project.views.calq_sigy', route_name = 'calq_sigy')

    config.add_route('drvzdy', '/drvzdy')
    config.add_view('cta_project.views.drvzdy', route_name = 'drvzdy')
	
    config.add_route('drvdev_daqy', '/drvdev_daqy')
    config.add_view('cta_project.views.drvdev_daqy', route_name = 'drvdev_daqy')	
	
    config.add_route('camhv_daqy', '/camhv_daqy')
    config.add_view('cta_project.views.camhv_daqy', route_name = 'camhv_daqy')	
	
    config.add_route('camdc_daqy', '/camdc_daqy')
    config.add_view('cta_project.views.camdc_daqy', route_name = 'camdc_daqy')
	
    config.add_route('camdt_daqy', '/camdt_daqy')
    config.add_view('cta_project.views.camdt_daqy', route_name = 'camdt_daqy')	
	
    config.add_route('campd_daqy', '/campd_daqy')
    config.add_view('cta_project.views.campd_daqy', route_name = 'campd_daqy')
	
    config.add_route('campixtemp_daqy', '/campixtemp_daqy')
    config.add_view('cta_project.views.campixtemp_daqy', route_name = 'campixtemp_daqy')
	
    config.add_route('meanpixtemp_daqy', '/meanpixtemp_daqy')
    config.add_view('cta_project.views.meanpixtemp_daqy', route_name = 'meanpixtemp_daqy')	
	
    config.add_route('camclusttempy', '/camclusttempy')
    config.add_view('cta_project.views.camclusttempy', route_name = 'camclusttempy')

    config.add_route('camvcelbias_daqy', '/camvcelbias_daqy')
    config.add_view('cta_project.views.camvcelbias_daqy', route_name = 'camvcelbias_daqy')
	
    config.add_route('camlv1tempy', '/camlv1tempy')
    config.add_view('cta_project.views.camlv1tempy', route_name = 'camlv1tempy')	
	
    config.add_route('camlv2tempy', '/camlv2tempy')
    config.add_view('cta_project.views.camlv2tempy', route_name = 'camlv2tempy')	
	
    config.add_route('camlv1humy', '/camlv1humy')
    config.add_view('cta_project.views.camlv1humy', route_name = 'camlv1humy')
	
    config.add_route('camlv2humy', '/camlv2humy')
    config.add_view('cta_project.views.camlv2humy', route_name = 'camlv2humy')	
	
    config.add_route('camcoolfcptoplefty', '/camcoolfcptoplefty')
    config.add_view('cta_project.views.camcoolfcptoplefty', route_name = 'camcoolfcptoplefty')
	
    config.add_route('camcoolfcpbottrighty', '/camcoolfcpbottrighty')
    config.add_view('cta_project.views.camcoolfcpbottrighty', route_name = 'camcoolfcpbottrighty')
	
    config.add_route('camcoolrcptoplefty', '/camcoolrcptoplefty')
    config.add_view('cta_project.views.camcoolrcptoplefty', route_name = 'camcoolrcptoplefty')	
	
    config.add_route('camcoolrcpbottrighty', '/camcoolrcpbottrighty')
    config.add_view('cta_project.views.camcoolrcpbottrighty', route_name = 'camcoolrcpbottrighty')

    config.add_route('camcoolchasiastoplefty', '/camcoolchasiastoplefty')
    config.add_view('cta_project.views.camcoolchasiastoplefty', route_name = 'camcoolchasiastoplefty')
	
    config.add_route('camcoolchasiasbottrighty', '/camcoolchasiasbottrighty')
    config.add_view('cta_project.views.camcoolchasiasbottrighty', route_name = 'camcoolchasiasbottrighty')	
	
    config.add_route('camcoolchasiasftoplefty', '/camcoolchasiasftoplefty')
    config.add_view('cta_project.views.camcoolchasiasftoplefty', route_name = 'camcoolchasiasftoplefty')	
	
    config.add_route('camcoolchasiasfbottrighty', '/camcoolchasiasfbottrighty')
    config.add_view('cta_project.views.camcoolchasiasfbottrighty', route_name = 'camcoolchasiasfbottrighty')
	
    config.add_route('camcoolrearbottlefty', '/camcoolrearbottlefty')
    config.add_view('cta_project.views.camcoolrearbottlefty', route_name = 'camcoolrearbottlefty')	
	
    config.add_route('camcoolreartoplefty', '/camcoolreartoplefty')
    config.add_view('cta_project.views.camcoolreartoplefty', route_name = 'camcoolreartoplefty')
	
    config.add_route('camcoolfrontbottrighty', '/camcoolfrontbottrighty')
    config.add_view('cta_project.views.camcoolfrontbottrighty', route_name = 'camcoolfrontbottrighty')
	
    config.add_route('camcoolfronttoprighty', '/camcoolfronttoprighty')
    config.add_view('cta_project.views.camcoolfronttoprighty', route_name = 'camcoolfronttoprighty')	
	
    config.add_route('amcerry', '/amcerry')
    config.add_view('cta_project.views.amcerry', route_name = 'amcerry')

    config.add_route('l1ty', '/l1ty')
    config.add_view('cta_project.views.l1ty', route_name = 'l1ty')
	
    config.add_route('l2ty', '/l2ty')
    config.add_view('cta_project.views.l2ty', route_name = 'l2ty')	
	
    config.add_route('l2t_daqy', '/l2t_daqy')
    config.add_view('cta_project.views.l2t_daqy', route_name = 'l2t_daqy')	
	
    config.add_route('sumt_globry', '/sumt_globry')
    config.add_view('cta_project.views.sumt_globry', route_name = 'sumt_globry')
	
    config.add_route('sumt_l3y', '/sumt_l3y')
    config.add_view('cta_project.views.sumt_l3y', route_name = 'sumt_l3y')	
	
    config.add_route('sumt_dtwy', '/sumt_dtwy')
    config.add_view('cta_project.views.sumt_dtwy', route_name = 'sumt_dtwy')
	
    config.add_route('sumt_cbt1y', '/sumt_cbt1y')
    config.add_view('cta_project.views.sumt_cbt1y', route_name = 'sumt_cbt1y')
	
    config.add_route('sumt_cbt2y', '/sumt_cbt2y')
    config.add_view('cta_project.views.sumt_cbt2y', route_name = 'sumt_cbt2y')	
	
    config.add_route('sumt_acy', '/sumt_acy')
    config.add_view('cta_project.views.sumt_acy', route_name = 'sumt_acy')
	
    config.add_route('sumt_astroby', '/sumt_astroby')
    config.add_view('cta_project.views.sumt_astroby', route_name = 'sumt_astroby')
	
    config.add_route('cool_cratey', '/cool_cratey')
    config.add_view('cta_project.views.cool_cratey', route_name = 'cool_cratey')	
	
    config.add_route('cool_racky', '/cool_racky')
    config.add_view('cta_project.views.cool_racky', route_name = 'cool_racky')	
	
    config.add_route('calbtemp1y', '/calbtemp1y')
    config.add_view('cta_project.views.calbtemp1y', route_name = 'calbtemp1y')
	
    config.add_route('calbtemp2y', '/calbtemp2y')
    config.add_view('cta_project.views.calbtemp2y', route_name = 'calbtemp2y')	
	
    config.add_route('calbhumy', '/calbhumy')
    config.add_view('cta_project.views.calbhumy', route_name = 'calbhumy')
	
    config.add_route('sg_devazy', '/sg_devazy')
    config.add_view('cta_project.views.sg_devazy', route_name = 'sg_devazy')
	
    config.add_route('sg_devzdy', '/sg_devzdy')
    config.add_view('cta_project.views.sg_devzdy', route_name = 'sg_devzdy')	
	
    config.add_route('sg_camcxy', '/sg_camcxy')
    config.add_view('cta_project.views.sg_camcxy', route_name = 'sg_camcxy')

    config.add_route('sg_camcyy', '/sg_camcyy')
    config.add_view('cta_project.views.sg_camcyy', route_name = 'sg_camcyy')
	
    config.add_route('sg_starsy', '/sg_starsy')
    config.add_view('cta_project.views.sg_starsy', route_name = 'sg_starsy')	
	
    config.add_route('sg_brighty', '/sg_brighty')
    config.add_view('cta_project.views.sg_brighty', route_name = 'sg_brighty')	
	
    config.add_route('wea_tempy', '/wea_tempy')
    config.add_view('cta_project.views.wea_tempy', route_name = 'wea_tempy')
	
    config.add_route('pyro_cloudy', '/pyro_cloudy')
    config.add_view('cta_project.views.pyro_cloudy', route_name = 'pyro_cloudy')	
	
    config.add_route('pyro_skyty', '/pyro_skyty')
    config.add_view('cta_project.views.pyro_skyty', route_name = 'pyro_skyty')
	
    config.add_route('las_trans3kmy', '/las_trans3kmy')
    config.add_view('cta_project.views.las_trans3kmy', route_name = 'las_trans3kmy')
	
    config.add_route('las_trans6kmy', '/las_trans6kmy')
    config.add_view('cta_project.views.las_trans6kmy', route_name = 'las_trans6kmy')	
	
    config.add_route('las_trans9kmy', '/las_trans9kmy')
    config.add_view('cta_project.views.las_trans9kmy', route_name = 'las_trans9kmy')
	
    config.add_route('las_trans12kmy', '/las_trans12kmy')
    config.add_view('cta_project.views.las_trans12kmy', route_name = 'las_trans12kmy')
	
    config.add_route('muon_psfy', '/muon_psfy')
    config.add_view('cta_project.views.muon_psfy', route_name = 'muon_psfy')	
	
    config.add_route('muon_psfny', '/muon_psfny')
    config.add_view('cta_project.views.muon_psfny', route_name = 'muon_psfny')	
	
    config.add_route('muon_sizey', '/muon_sizey')
    config.add_view('cta_project.views.muon_sizey', route_name = 'muon_sizey')
	
    config.add_route('sbigpsf_by', '/sbigpsf_by')
    config.add_view('cta_project.views.sbigpsf_by', route_name = 'sbigpsf_by')	
	
    config.add_route('sbigpsf_ly', '/sbigpsf_ly')
    config.add_view('cta_project.views.sbigpsf_ly', route_name = 'sbigpsf_ly')
	
    config.add_route('bias_sigy', '/bias_sigy')
    config.add_view('cta_project.views.bias_sigy', route_name = 'bias_sigy')	
	
    config.add_route('hitfrac_sigy', '/hitfrac_sigy')
    config.add_view('cta_project.views.hitfrac_sigy', route_name = 'hitfrac_sigy')
	
    config.add_route('arrtm_caly', '/arrtm_caly')
    config.add_view('cta_project.views.arrtm_caly', route_name = 'arrtm_caly')	
	
    config.add_route('arrtm_inty', '/arrtm_inty')
    config.add_view('cta_project.views.arrtm_inty', route_name = 'arrtm_inty')
	
    config.add_route('arrtm_sigy', '/arrtm_sigy')
    config.add_view('cta_project.views.arrtm_sigy', route_name = 'arrtm_sigy')
	
    config.add_route('arrtmrms_caly', '/arrtmrms_caly')
    config.add_view('cta_project.views.arrtmrms_caly', route_name = 'arrtmrms_caly')	
	
    config.add_route('arrtmrms_inty', '/arrtmrms_inty')
    config.add_view('cta_project.views.arrtmrms_inty', route_name = 'arrtmrms_inty')
	
    config.add_route('arrtmrms_sigy', '/arrtmrms_sigy')
    config.add_view('cta_project.views.arrtmrms_sigy', route_name = 'arrtmrms_sigy')
	
    config.add_route('ped_pedy', '/ped_pedy')
    config.add_view('cta_project.views.ped_pedy', route_name = 'ped_pedy')	
	
    config.add_route('ped_inty', '/ped_inty')
    config.add_view('cta_project.views.ped_inty', route_name = 'ped_inty')	
	
    config.add_route('npe_inty', '/npe_inty')
    config.add_view('cta_project.views.npe_inty', route_name = 'npe_inty')
	
    config.add_route('pedrms_pedy', '/pedrms_pedy')
    config.add_view('cta_project.views.pedrms_pedy', route_name = 'pedrms_pedy')	
	
    config.add_route('pedrms_inty', '/pedrms_inty')
    config.add_view('cta_project.views.pedrms_inty', route_name = 'pedrms_inty')

    config.add_route('cfact_inty', '/cfact_inty')
    config.add_view('cta_project.views.cfact_inty', route_name = 'cfact_inty')
    config.add_route('wea_wsM2', '/wea_wsM2')
    config.add_view('cta_project.views.wea_wsM2', route_name = 'wea_wsM2')
    config.add_route('wea_humM2', '/wea_humM2M2')
    config.add_view('cta_project.views.wea_humM2', route_name = 'wea_humM2')
    config.add_route('wea_gustM2', '/wea_gustM2')
    config.add_view('cta_project.views.wea_gustM2', route_name = 'wea_gustM2')
	
    config.add_route('wea_seeM2', '/wea_seeM2')
    config.add_view('cta_project.views.wea_seeM2', route_name = 'wea_seeM2')
	
    config.add_route('wea_dustM2', '/wea_dustM2')
    config.add_view('cta_project.views.wea_dustM2', route_name = 'wea_dustM2')	
	
    config.add_route('rec_tempM2', '/rec_tempM2')
    config.add_view('cta_project.views.rec_tempM2', route_name = 'rec_tempM2')	
	
    config.add_route('camtd_daqM2', '/camtd_daqM2')
    config.add_view('cta_project.views.camtd_daqM2', route_name = 'camtd_daqM2')
	
    config.add_route('camipr_daqM2', '/camipr_daqM2')
    config.add_view('cta_project.views.camipr_daqM2', route_name = 'camipr_daqM2')	
	
    config.add_route('camiprerr_daqM2', '/camiprerr_daqM2')
    config.add_view('cta_project.views.camiprerr_daqM2', route_name = 'camiprerr_daqM2')
	
    config.add_route('calq_calM2', '/calq_calM2')
    config.add_view('cta_project.views.calq_calM2', route_name = 'calq_calM2')
	
    config.add_route('calq_intM2', '/calq_intM2')
    config.add_view('cta_project.views.calq_intM2', route_name = 'calq_intM2')	
	
    config.add_route('calq_sigM2', '/calq_sigM2')
    config.add_view('cta_project.views.calq_sigM2', route_name = 'calq_sigM2')

    config.add_route('drvzdM2', '/drvzdM2')
    config.add_view('cta_project.views.drvzdM2', route_name = 'drvzdM2')
	
    config.add_route('drvdev_daqM2', '/drvdev_daqM2')
    config.add_view('cta_project.views.drvdev_daqM2', route_name = 'drvdev_daqM2')	
	
    config.add_route('camhv_daqM2', '/camhv_daqM2')
    config.add_view('cta_project.views.camhv_daqM2', route_name = 'camhv_daqM2')	
	
    config.add_route('camdc_daqM2', '/camdc_daqM2')
    config.add_view('cta_project.views.camdc_daqM2', route_name = 'camdc_daqM2')
	
    config.add_route('camdt_daqM2', '/camdt_daqM2')
    config.add_view('cta_project.views.camdt_daqM2', route_name = 'camdt_daqM2')	
	
    config.add_route('campd_daqM2', '/campd_daqM2')
    config.add_view('cta_project.views.campd_daqM2', route_name = 'campd_daqM2')
	
    config.add_route('campixtemp_daqM2', '/campixtemp_daqM2')
    config.add_view('cta_project.views.campixtemp_daqM2', route_name = 'campixtemp_daqM2')
	
    config.add_route('meanpixtemp_daqM2', '/meanpixtemp_daqM2')
    config.add_view('cta_project.views.meanpixtemp_daqM2', route_name = 'meanpixtemp_daqM2')	
	
    config.add_route('camclusttempM2', '/camclusttempM2')
    config.add_view('cta_project.views.camclusttempM2', route_name = 'camclusttempM2')

    config.add_route('camvcelbias_daqM2', '/camvcelbias_daqM2')
    config.add_view('cta_project.views.camvcelbias_daqM2', route_name = 'camvcelbias_daqM2')
	
    config.add_route('camlv1tempM2', '/camlv1tempM2')
    config.add_view('cta_project.views.camlv1tempM2', route_name = 'camlv1tempM2')	
	
    config.add_route('camlv2tempM2', '/camlv2tempM2')
    config.add_view('cta_project.views.camlv2tempM2', route_name = 'camlv2tempM2')	
	
    config.add_route('camlv1humM2', '/camlv1humM2')
    config.add_view('cta_project.views.camlv1humM2', route_name = 'camlv1humM2')
	
    config.add_route('camlv2humM2', '/camlv2humM2')
    config.add_view('cta_project.views.camlv2humM2', route_name = 'camlv2humM2')	
	
    config.add_route('camcoolfcptopleftM2', '/camcoolfcptopleftM2')
    config.add_view('cta_project.views.camcoolfcptopleftM2', route_name = 'camcoolfcptopleftM2')
	
    config.add_route('camcoolfcpbottrightM2', '/camcoolfcpbottrightM2')
    config.add_view('cta_project.views.camcoolfcpbottrightM2', route_name = 'camcoolfcpbottrightM2')
	
    config.add_route('camcoolrcptopleftM2', '/camcoolrcptopleftM2')
    config.add_view('cta_project.views.camcoolrcptopleftM2', route_name = 'camcoolrcptopleftM2')	
	
    config.add_route('camcoolrcpbottrightM2', '/camcoolrcpbottrightM2')
    config.add_view('cta_project.views.camcoolrcpbottrightM2', route_name = 'camcoolrcpbottrightM2')

    config.add_route('camcoolchasiastopleftM2', '/camcoolchasiastopleftM2')
    config.add_view('cta_project.views.camcoolchasiastopleftM2', route_name = 'camcoolchasiastopleftM2')
	
    config.add_route('camcoolchasiasbottrightM2', '/camcoolchasiasbottrightM2')
    config.add_view('cta_project.views.camcoolchasiasbottrightM2', route_name = 'camcoolchasiasbottrightM2')	
	
    config.add_route('camcoolchasiasftopleftM2', '/camcoolchasiasftopleftM2')
    config.add_view('cta_project.views.camcoolchasiasftopleftM2', route_name = 'camcoolchasiasftopleftM2')	
	
    config.add_route('camcoolchasiasfbottrightM2', '/camcoolchasiasfbottrightM2')
    config.add_view('cta_project.views.camcoolchasiasfbottrightM2', route_name = 'camcoolchasiasfbottrightM2')
	
    config.add_route('camcoolrearbottleftM2', '/camcoolrearbottleftM2')
    config.add_view('cta_project.views.camcoolrearbottleftM2', route_name = 'camcoolrearbottleftM2')	
	
    config.add_route('camcoolreartopleftM2', '/camcoolreartopleftM2')
    config.add_view('cta_project.views.camcoolreartopleftM2', route_name = 'camcoolreartopleftM2')
	
    config.add_route('camcoolfrontbottrightM2', '/camcoolfrontbottrightM2')
    config.add_view('cta_project.views.camcoolfrontbottrightM2', route_name = 'camcoolfrontbottrightM2')
	
    config.add_route('camcoolfronttoprightM2', '/camcoolfronttoprightM2')
    config.add_view('cta_project.views.camcoolfronttoprightM2', route_name = 'camcoolfronttoprightM2')	
	
    config.add_route('amcerrM2', '/amcerrM2')
    config.add_view('cta_project.views.amcerrM2', route_name = 'amcerrM2')

    config.add_route('l1tM2', '/l1tM2')
    config.add_view('cta_project.views.l1tM2', route_name = 'l1tM2')
	
    config.add_route('l2tM2', '/l2tM2')
    config.add_view('cta_project.views.l2tM2', route_name = 'l2tM2')	
	
    config.add_route('l2t_daqM2', '/l2t_daqM2')
    config.add_view('cta_project.views.l2t_daqM2', route_name = 'l2t_daqM2')	
	
    config.add_route('sumt_globrM2', '/sumt_globrM2')
    config.add_view('cta_project.views.sumt_globrM2', route_name = 'sumt_globrM2')
	
    config.add_route('sumt_l3M2', '/sumt_l3M2')
    config.add_view('cta_project.views.sumt_l3M2', route_name = 'sumt_l3M2')	
	
    config.add_route('sumt_dtwM2', '/sumt_dtwM2')
    config.add_view('cta_project.views.sumt_dtwM2', route_name = 'sumt_dtwM2')
	
    config.add_route('sumt_cbt1M2', '/sumt_cbt1M2')
    config.add_view('cta_project.views.sumt_cbt1M2', route_name = 'sumt_cbt1M2')
	
    config.add_route('sumt_cbt2M2', '/sumt_cbt2M2')
    config.add_view('cta_project.views.sumt_cbt2M2', route_name = 'sumt_cbt2M2')	
	
    config.add_route('sumt_acM2', '/sumt_acM2')
    config.add_view('cta_project.views.sumt_acM2', route_name = 'sumt_acM2')
	
    config.add_route('sumt_astrobM2', '/sumt_astrobM2')
    config.add_view('cta_project.views.sumt_astrobM2', route_name = 'sumt_astrobM2')
	
    config.add_route('cool_crateM2', '/cool_crateM2')
    config.add_view('cta_project.views.cool_crateM2', route_name = 'cool_crateM2')	
	
    config.add_route('cool_rackM2', '/cool_rackM2')
    config.add_view('cta_project.views.cool_rackM2', route_name = 'cool_rackM2')	
	
    config.add_route('calbtemp1M2', '/calbtemp1M2')
    config.add_view('cta_project.views.calbtemp1M2', route_name = 'calbtemp1M2')
	
    config.add_route('calbtemp2M2', '/calbtemp2M2')
    config.add_view('cta_project.views.calbtemp2M2', route_name = 'calbtemp2M2')	
	
    config.add_route('calbhumM2', '/calbhumM2')
    config.add_view('cta_project.views.calbhumM2', route_name = 'calbhumM2')
	
    config.add_route('sg_devazM2', '/sg_devazM2')
    config.add_view('cta_project.views.sg_devazM2', route_name = 'sg_devazM2')
	
    config.add_route('sg_devzdM2', '/sg_devzdM2')
    config.add_view('cta_project.views.sg_devzdM2', route_name = 'sg_devzdM2')	
	
    config.add_route('sg_camcxM2', '/sg_camcxM2')
    config.add_view('cta_project.views.sg_camcxM2', route_name = 'sg_camcxM2')

    config.add_route('sg_camcyM2', '/sg_camcyM2')
    config.add_view('cta_project.views.sg_camcyM2', route_name = 'sg_camcyM2')
	
    config.add_route('sg_starsM2', '/sg_starsM2')
    config.add_view('cta_project.views.sg_starsM2', route_name = 'sg_starsM2')	
	
    config.add_route('sg_brightM2', '/sg_brightM2')
    config.add_view('cta_project.views.sg_brightM2', route_name = 'sg_brightM2')	
	
    config.add_route('wea_tempM2', '/wea_tempM2')
    config.add_view('cta_project.views.wea_tempM2', route_name = 'wea_tempM2')
	
    config.add_route('pyro_cloudM2', '/pyro_cloudM2')
    config.add_view('cta_project.views.pyro_cloudM2', route_name = 'pyro_cloudM2')	
	
    config.add_route('pyro_skytM2', '/pyro_skytM2')
    config.add_view('cta_project.views.pyro_skytM2', route_name = 'pyro_skytM2')
	
    config.add_route('las_trans3kmM2', '/las_trans3kmM2')
    config.add_view('cta_project.views.las_trans3kmM2', route_name = 'las_trans3kmM2')
	
    config.add_route('las_trans6kmM2', '/las_trans6kmM2')
    config.add_view('cta_project.views.las_trans6kmM2', route_name = 'las_trans6kmM2')	
	
    config.add_route('las_trans9kmM2', '/las_trans9kmM2')
    config.add_view('cta_project.views.las_trans9kmM2', route_name = 'las_trans9kmM2')
	
    config.add_route('las_trans12kmM2', '/las_trans12kmM2')
    config.add_view('cta_project.views.las_trans12kmM2', route_name = 'las_trans12kmM2')
	
    config.add_route('muon_psfM2', '/muon_psfM2')
    config.add_view('cta_project.views.muon_psfM2', route_name = 'muon_psfM2')	
	
    config.add_route('muon_psfnM2', '/muon_psfnM2')
    config.add_view('cta_project.views.muon_psfnM2', route_name = 'muon_psfnM2')	
	
    config.add_route('muon_sizeM2', '/muon_sizeM2')
    config.add_view('cta_project.views.muon_sizeM2', route_name = 'muon_sizeM2')
	
    config.add_route('sbigpsf_bM2', '/sbigpsf_bM2')
    config.add_view('cta_project.views.sbigpsf_bM2', route_name = 'sbigpsf_bM2')	
	
    config.add_route('sbigpsf_lM2', '/sbigpsf_lM2')
    config.add_view('cta_project.views.sbigpsf_lM2', route_name = 'sbigpsf_lM2')
	
    config.add_route('bias_sigM2', '/bias_sigM2')
    config.add_view('cta_project.views.bias_sigM2', route_name = 'bias_sigM2')	
	
    config.add_route('hitfrac_sigM2', '/hitfrac_sigM2')
    config.add_view('cta_project.views.hitfrac_sigM2', route_name = 'hitfrac_sigM2')
	
    config.add_route('arrtm_calM2', '/arrtm_calM2')
    config.add_view('cta_project.views.arrtm_calM2', route_name = 'arrtm_calM2')	
	
    config.add_route('arrtm_intM2', '/arrtm_intM2')
    config.add_view('cta_project.views.arrtm_intM2', route_name = 'arrtm_intM2')
	
    config.add_route('arrtm_sigM2', '/arrtm_sigM2')
    config.add_view('cta_project.views.arrtm_sigM2', route_name = 'arrtm_sigM2')
	
    config.add_route('arrtmrms_calM2', '/arrtmrms_calM2')
    config.add_view('cta_project.views.arrtmrms_calM2', route_name = 'arrtmrms_calM2')	
	
    config.add_route('arrtmrms_intM2', '/arrtmrms_intM2')
    config.add_view('cta_project.views.arrtmrms_intM2', route_name = 'arrtmrms_intM2')
	
    config.add_route('arrtmrms_sigM2', '/arrtmrms_sigM2')
    config.add_view('cta_project.views.arrtmrms_sigM2', route_name = 'arrtmrms_sigM2')
	
    config.add_route('ped_pedM2', '/ped_pedM2')
    config.add_view('cta_project.views.ped_pedM2', route_name = 'ped_pedM2')	
	
    config.add_route('ped_intM2', '/ped_intM2')
    config.add_view('cta_project.views.ped_intM2', route_name = 'ped_intM2')	
	
    config.add_route('npe_intM2', '/npe_intM2')
    config.add_view('cta_project.views.npe_intM2', route_name = 'npe_intM2')
	
    config.add_route('pedrms_pedM2', '/pedrms_pedM2')
    config.add_view('cta_project.views.pedrms_pedM2', route_name = 'pedrms_pedM2')	
	
    config.add_route('pedrms_intM2', '/pedrms_intM2')
    config.add_view('cta_project.views.pedrms_intM2', route_name = 'pedrms_intM2')

    config.add_route('cfact_intM2', '/cfact_intM2')
    config.add_view('cta_project.views.cfact_intM2', route_name = 'cfact_intM2')
    config.add_route('wea_wsyM2', '/wea_wsyM2')	
    config.add_view('cta_project.views.wea_wsyM2', route_name = 'wea_wsyM2')
    config.add_route('wea_humyM2', '/wea_humyM2')
    config.add_view('cta_project.views.wea_humyM2', route_name = 'wea_humyM2')
    config.add_route('wea_gustyM2', '/wea_gustyM2')
    config.add_view('cta_project.views.wea_gustyM2', route_name = 'wea_gustyM2')
	
    config.add_route('wea_seeyM2', '/wea_seeyM2')
    config.add_view('cta_project.views.wea_seeyM2', route_name = 'wea_seeyM2')
	
    config.add_route('wea_dustyM2', '/wea_dustyM2')
    config.add_view('cta_project.views.wea_dustyM2', route_name = 'wea_dustyM2')	
	
    config.add_route('rec_tempyM2', '/rec_tempyM2')
    config.add_view('cta_project.views.rec_tempyM2', route_name = 'rec_tempyM2')	
	
    config.add_route('camtd_daqyM2', '/camtd_daqyM2')
    config.add_view('cta_project.views.camtd_daqyM2', route_name = 'camtd_daqyM2')
	
    config.add_route('camipr_daqyM2', '/camipr_daqyM2')
    config.add_view('cta_project.views.camipr_daqyM2', route_name = 'camipr_daqyM2')	
	
    config.add_route('camiprerr_daqyM2', '/camiprerr_daqyM2')
    config.add_view('cta_project.views.camiprerr_daqyM2', route_name = 'camiprerr_daqyM2')
	
    config.add_route('calq_calyM2', '/calq_calyM2')
    config.add_view('cta_project.views.calq_calyM2', route_name = 'calq_calyM2')
	
    config.add_route('calq_intyM2', '/calq_intyM2')
    config.add_view('cta_project.views.calq_intyM2', route_name = 'calq_intyM2')	
	
    config.add_route('calq_sigyM2', '/calq_sigyM2')
    config.add_view('cta_project.views.calq_sigyM2', route_name = 'calq_sigyM2')

    config.add_route('drvzdyM2', '/drvzdyM2')
    config.add_view('cta_project.views.drvzdyM2', route_name = 'drvzdyM2')
	
    config.add_route('drvdev_daqyM2', '/drvdev_daqyM2')
    config.add_view('cta_project.views.drvdev_daqyM2', route_name = 'drvdev_daqyM2')	
	
    config.add_route('camhv_daqyM2', '/camhv_daqyM2')
    config.add_view('cta_project.views.camhv_daqyM2', route_name = 'camhv_daqyM2')	
	
    config.add_route('camdc_daqyM2', '/camdc_daqyM2')
    config.add_view('cta_project.views.camdc_daqyM2', route_name = 'camdc_daqyM2')
	
    config.add_route('camdt_daqyM2', '/camdt_daqyM2')
    config.add_view('cta_project.views.camdt_daqyM2', route_name = 'camdt_daqyM2')	
	
    config.add_route('campd_daqyM2', '/campd_daqyM2')
    config.add_view('cta_project.views.campd_daqyM2', route_name = 'campd_daqyM2')
	
    config.add_route('campixtemp_daqyM2', '/campixtemp_daqyM2')
    config.add_view('cta_project.views.campixtemp_daqyM2', route_name = 'campixtemp_daqyM2')
	
    config.add_route('meanpixtemp_daqyM2', '/meanpixtemp_daqyM2')
    config.add_view('cta_project.views.meanpixtemp_daqyM2', route_name = 'meanpixtemp_daqyM2')	
	
    config.add_route('camclusttempyM2', '/camclusttempyM2')
    config.add_view('cta_project.views.camclusttempyM2', route_name = 'camclusttempyM2')

    config.add_route('camvcelbias_daqyM2', '/camvcelbias_daqyM2')
    config.add_view('cta_project.views.camvcelbias_daqyM2', route_name = 'camvcelbias_daqyM2')
	
    config.add_route('camlv1tempyM2', '/camlv1tempyM2')
    config.add_view('cta_project.views.camlv1tempyM2', route_name = 'camlv1tempyM2')	
	
    config.add_route('camlv2tempyM2', '/camlv2tempyM2')
    config.add_view('cta_project.views.camlv2tempyM2', route_name = 'camlv2tempyM2')	
	
    config.add_route('camlv1humyM2', '/camlv1humyM2')
    config.add_view('cta_project.views.camlv1humyM2', route_name = 'camlv1humyM2')
	
    config.add_route('camlv2humyM2', '/camlv2humyM2')
    config.add_view('cta_project.views.camlv2humyM2', route_name = 'camlv2humyM2')	
	
    config.add_route('camcoolfcptopleftyM2', '/camcoolfcptopleftyM2')
    config.add_view('cta_project.views.camcoolfcptopleftyM2', route_name = 'camcoolfcptopleftyM2')
	
    config.add_route('camcoolfcpbottrightyM2', '/camcoolfcpbottrightyM2')
    config.add_view('cta_project.views.camcoolfcpbottrightyM2', route_name = 'camcoolfcpbottrightyM2')
	
    config.add_route('camcoolrcptopleftyM2', '/camcoolrcptopleftyM2')
    config.add_view('cta_project.views.camcoolrcptopleftyM2', route_name = 'camcoolrcptopleftyM2')	
	
    config.add_route('camcoolrcpbottrightyM2', '/camcoolrcpbottrightyM2')
    config.add_view('cta_project.views.camcoolrcpbottrightyM2', route_name = 'camcoolrcpbottrightyM2')

    config.add_route('camcoolchasiastopleftyM2', '/camcoolchasiastopleftyM2')
    config.add_view('cta_project.views.camcoolchasiastopleftyM2', route_name = 'camcoolchasiastopleftyM2')
	
    config.add_route('camcoolchasiasbottrightyM2', '/camcoolchasiasbottrightyM2')
    config.add_view('cta_project.views.camcoolchasiasbottrightyM2', route_name = 'camcoolchasiasbottrightyM2')	
	
    config.add_route('camcoolchasiasftopleftyM2', '/camcoolchasiasftopleftyM2')
    config.add_view('cta_project.views.camcoolchasiasftopleftyM2', route_name = 'camcoolchasiasftopleftyM2')	
	
    config.add_route('camcoolchasiasfbottrightyM2', '/camcoolchasiasfbottrightyM2')
    config.add_view('cta_project.views.camcoolchasiasfbottrightyM2', route_name = 'camcoolchasiasfbottrightyM2')
	
    config.add_route('camcoolrearbottleftyM2', '/camcoolrearbottleftyM2')
    config.add_view('cta_project.views.camcoolrearbottleftyM2', route_name = 'camcoolrearbottleftyM2')	
	
    config.add_route('camcoolreartopleftyM2', '/camcoolreartopleftyM2')
    config.add_view('cta_project.views.camcoolreartopleftyM2', route_name = 'camcoolreartopleftyM2')
	
    config.add_route('camcoolfrontbottrightyM2', '/camcoolfrontbottrightyM2')
    config.add_view('cta_project.views.camcoolfrontbottrightyM2', route_name = 'camcoolfrontbottrightyM2')
	
    config.add_route('camcoolfronttoprightyM2', '/camcoolfronttoprightyM2')
    config.add_view('cta_project.views.camcoolfronttoprightyM2', route_name = 'camcoolfronttoprightyM2')	
	
    config.add_route('amcerryM2', '/amcerryM2')
    config.add_view('cta_project.views.amcerryM2', route_name = 'amcerryM2')

    config.add_route('l1tyM2', '/l1tyM2')
    config.add_view('cta_project.views.l1tyM2', route_name = 'l1tyM2')
	
    config.add_route('l2tyM2', '/l2tyM2')
    config.add_view('cta_project.views.l2tyM2', route_name = 'l2tyM2')	
	
    config.add_route('l2t_daqyM2', '/l2t_daqyM2')
    config.add_view('cta_project.views.l2t_daqyM2', route_name = 'l2t_daqyM2')	
	
    config.add_route('sumt_globryM2', '/sumt_globryM2')
    config.add_view('cta_project.views.sumt_globryM2', route_name = 'sumt_globryM2')
	
    config.add_route('sumt_l3yM2', '/sumt_l3yM2')
    config.add_view('cta_project.views.sumt_l3yM2', route_name = 'sumt_l3yM2')	
	
    config.add_route('sumt_dtwyM2', '/sumt_dtwyM2')
    config.add_view('cta_project.views.sumt_dtwyM2', route_name = 'sumt_dtwyM2')
	
    config.add_route('sumt_cbt1yM2', '/sumt_cbt1yM2')
    config.add_view('cta_project.views.sumt_cbt1yM2', route_name = 'sumt_cbt1yM2')
	
    config.add_route('sumt_cbt2yM2', '/sumt_cbt2yM2')
    config.add_view('cta_project.views.sumt_cbt2yM2', route_name = 'sumt_cbt2yM2')	
	
    config.add_route('sumt_acyM2', '/sumt_acyM2')
    config.add_view('cta_project.views.sumt_acyM2', route_name = 'sumt_acyM2')
	
    config.add_route('sumt_astrobyM2', '/sumt_astrobyM2')
    config.add_view('cta_project.views.sumt_astrobyM2', route_name = 'sumt_astrobyM2')
	
    config.add_route('cool_crateyM2', '/cool_crateyM2')
    config.add_view('cta_project.views.cool_crateyM2', route_name = 'cool_crateyM2')	
	
    config.add_route('cool_rackyM2', '/cool_rackyM2')
    config.add_view('cta_project.views.cool_rackyM2', route_name = 'cool_rackyM2')	
	
    config.add_route('calbtemp1yM2', '/calbtemp1yM2')
    config.add_view('cta_project.views.calbtemp1yM2', route_name = 'calbtemp1yM2')
	
    config.add_route('calbtemp2yM2', '/calbtemp2yM2')
    config.add_view('cta_project.views.calbtemp2yM2', route_name = 'calbtemp2yM2')	
	
    config.add_route('calbhumyM2', '/calbhumyM2')
    config.add_view('cta_project.views.calbhumyM2', route_name = 'calbhumyM2')
	
    config.add_route('sg_devazyM2', '/sg_devazyM2')
    config.add_view('cta_project.views.sg_devazyM2', route_name = 'sg_devazyM2')
	
    config.add_route('sg_devzdyM2', '/sg_devzdyM2')
    config.add_view('cta_project.views.sg_devzdyM2', route_name = 'sg_devzdyM2')	
	
    config.add_route('sg_camcxyM2', '/sg_camcxyM2')
    config.add_view('cta_project.views.sg_camcxyM2', route_name = 'sg_camcxyM2')

    config.add_route('sg_camcyyM2', '/sg_camcyyM2')
    config.add_view('cta_project.views.sg_camcyyM2', route_name = 'sg_camcyyM2')
	
    config.add_route('sg_starsyM2', '/sg_starsyM2')
    config.add_view('cta_project.views.sg_starsyM2', route_name = 'sg_starsyM2')	
	
    config.add_route('sg_brightyM2', '/sg_brightyM2')
    config.add_view('cta_project.views.sg_brightyM2', route_name = 'sg_brightyM2')	
	
    config.add_route('wea_tempyM2', '/wea_tempyM2')
    config.add_view('cta_project.views.wea_tempyM2', route_name = 'wea_tempyM2')
	
    config.add_route('pyro_cloudyM2', '/pyro_cloudyM2')
    config.add_view('cta_project.views.pyro_cloudyM2', route_name = 'pyro_cloudyM2')	
	
    config.add_route('pyro_skytyM2', '/pyro_skytyM2')
    config.add_view('cta_project.views.pyro_skytyM2', route_name = 'pyro_skytyM2')
	
    config.add_route('las_trans3kmyM2', '/las_trans3kmyM2')
    config.add_view('cta_project.views.las_trans3kmyM2', route_name = 'las_trans3kmyM2')
	
    config.add_route('las_trans6kmyM2', '/las_trans6kmyM2')
    config.add_view('cta_project.views.las_trans6kmyM2', route_name = 'las_trans6kmyM2')	
	
    config.add_route('las_trans9kmyM2', '/las_trans9kmyM2')
    config.add_view('cta_project.views.las_trans9kmyM2', route_name = 'las_trans9kmyM2')
	
    config.add_route('las_trans12kmyM2', '/las_trans12kmyM2')
    config.add_view('cta_project.views.las_trans12kmyM2', route_name = 'las_trans12kmyM2')
	
    config.add_route('muon_psfyM2', '/muon_psfyM2')
    config.add_view('cta_project.views.muon_psfyM2', route_name = 'muon_psfyM2')	
	
    config.add_route('muon_psfnyM2', '/muon_psfnyM2')
    config.add_view('cta_project.views.muon_psfnyM2', route_name = 'muon_psfnyM2')	
	
    config.add_route('muon_sizeyM2', '/muon_sizeyM2')
    config.add_view('cta_project.views.muon_sizeyM2', route_name = 'muon_sizeyM2')
	
    config.add_route('sbigpsf_byM2', '/sbigpsf_byM2')
    config.add_view('cta_project.views.sbigpsf_byM2', route_name = 'sbigpsf_byM2')	
	
    config.add_route('sbigpsf_lyM2', '/sbigpsf_lyM2')
    config.add_view('cta_project.views.sbigpsf_lyM2', route_name = 'sbigpsf_lyM2')
	
    config.add_route('bias_sigyM2', '/bias_sigyM2')
    config.add_view('cta_project.views.bias_sigyM2', route_name = 'bias_sigyM2')	
	
    config.add_route('hitfrac_sigyM2', '/hitfrac_sigyM2')
    config.add_view('cta_project.views.hitfrac_sigyM2', route_name = 'hitfrac_sigyM2')
	
    config.add_route('arrtm_calyM2', '/arrtm_calyM2')
    config.add_view('cta_project.views.arrtm_calyM2', route_name = 'arrtm_calyM2')	
	
    config.add_route('arrtm_intyM2', '/arrtm_intyM2')
    config.add_view('cta_project.views.arrtm_intyM2', route_name = 'arrtm_intyM2')
	
    config.add_route('arrtm_sigyM2', '/arrtm_sigyM2')
    config.add_view('cta_project.views.arrtm_sigyM2', route_name = 'arrtm_sigyM2')
	
    config.add_route('arrtmrms_calyM2', '/arrtmrms_calyM2')
    config.add_view('cta_project.views.arrtmrms_calyM2', route_name = 'arrtmrms_calyM2')	
	
    config.add_route('arrtmrms_intyM2', '/arrtmrms_intyM2')
    config.add_view('cta_project.views.arrtmrms_intyM2', route_name = 'arrtmrms_intyM2')
	
    config.add_route('arrtmrms_sigyM2', '/arrtmrms_sigyM2')
    config.add_view('cta_project.views.arrtmrms_sigyM2', route_name = 'arrtmrms_sigyM2')
	
    config.add_route('ped_pedyM2', '/ped_pedyM2')
    config.add_view('cta_project.views.ped_pedyM2', route_name = 'ped_pedyM2')	
	
    config.add_route('ped_intyM2', '/ped_intyM2')
    config.add_view('cta_project.views.ped_intyM2', route_name = 'ped_intyM2')	
	
    config.add_route('npe_intyM2', '/npe_intyM2')
    config.add_view('cta_project.views.npe_intyM2', route_name = 'npe_intyM2')
	
    config.add_route('pedrms_pedyM2', '/pedrms_pedyM2')
    config.add_view('cta_project.views.pedrms_pedyM2', route_name = 'pedrms_pedyM2')	
	
    config.add_route('pedrms_intyM2', '/pedrms_intyM2')
    config.add_view('cta_project.views.pedrms_intyM2', route_name = 'pedrms_intyM2')

    config.add_route('cfact_intyM2', '/cfact_intyM2')
    config.add_view('cta_project.views.cfact_intyM2', route_name = 'cfact_intyM2')	
    # MongoDB
    def add_mongo_db(event):
        settings = event.request.registry.settings
        url = settings['mongodb.url']
        db_name = settings['mongodb.db_name']
        db = settings['mongodb_conn'][db_name]
        event.request.db = db
    db_uri = settings['mongodb.url']
    MongoDB = pymongo.MongoClient
    if 'pyramid_debugtoolbar' in set(settings.values()):
        class MongoDB(pymongo.MongoClient):
            def __html__(self):
                return 'MongoDB: <b>{}></b>'.format(self)
    conn = MongoDB(db_uri)
    config.registry.settings['mongodb_conn'] = conn
    config.add_subscriber(add_mongo_db, NewRequest)
    config.scan('cta_project')
    return config.make_wsgi_app()
	
