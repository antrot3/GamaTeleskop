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
    config.add_view('cta_project.views.csvview', route_name = 'csv2')
    config.add_route('wea_ws', '/wea_ws')
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
    config.add_route('wea_wsmm', '/wea_wsmm')
    config.add_view('cta_project.views.wea_wsmm', route_name = 'wea_wsmm')
    config.add_route('wea_hummm', '/wea_hummm')
    config.add_view('cta_project.views.wea_hummm', route_name = 'wea_hummm')
    config.add_route('wea_gustmm', '/wea_gustmm')
    config.add_view('cta_project.views.wea_gustmm', route_name = 'wea_gustmm')
	
    config.add_route('wea_seemm', '/wea_seemm')
    config.add_view('cta_project.views.wea_seemm', route_name = 'wea_seemm')
	
    config.add_route('wea_dustmm', '/wea_dustmm')
    config.add_view('cta_project.views.wea_dustmm', route_name = 'wea_dustmm')	
	
    config.add_route('rec_tempmm', '/rec_tempmm')
    config.add_view('cta_project.views.rec_tempmm', route_name = 'rec_tempmm')	
	
    config.add_route('camtd_daqmm', '/camtd_daqmm')
    config.add_view('cta_project.views.camtd_daqmm', route_name = 'camtd_daqmm')
	
    config.add_route('camipr_daqmm', '/camipr_daqmm')
    config.add_view('cta_project.views.camipr_daqmm', route_name = 'camipr_daqmm')	
	
    config.add_route('camiprerr_daqmm', '/camiprerr_daqmm')
    config.add_view('cta_project.views.camiprerr_daqmm', route_name = 'camiprerr_daqmm')
	
    config.add_route('calq_calmm', '/calq_calmm')
    config.add_view('cta_project.views.calq_calmm', route_name = 'calq_calmm')
	
    config.add_route('calq_intmm', '/calq_intmm')
    config.add_view('cta_project.views.calq_intmm', route_name = 'calq_intmm')	
	
    config.add_route('calq_sigmm', '/calq_sigmm')
    config.add_view('cta_project.views.calq_sigmm', route_name = 'calq_sigmm')

    config.add_route('drvzdmm', '/drvzdmm')
    config.add_view('cta_project.views.drvzdmm', route_name = 'drvzdmm')
	
    config.add_route('drvdev_daqmm', '/drvdev_daqmm')
    config.add_view('cta_project.views.drvdev_daqmm', route_name = 'drvdev_daqmm')	
	
    config.add_route('camhv_daqmm', '/camhv_daqmm')
    config.add_view('cta_project.views.camhv_daqmm', route_name = 'camhv_daqmm')	
	
    config.add_route('camdc_daqmm', '/camdc_daqmm')
    config.add_view('cta_project.views.camdc_daqmm', route_name = 'camdc_daqmm')
	
    config.add_route('camdt_daqmm', '/camdt_daqmm')
    config.add_view('cta_project.views.camdt_daqmm', route_name = 'camdt_daqmm')	
	
    config.add_route('campd_daqmm', '/campd_daqmm')
    config.add_view('cta_project.views.campd_daqmm', route_name = 'campd_daqmm')
	
    config.add_route('campixtemp_daqmm', '/campixtemp_daqmm')
    config.add_view('cta_project.views.campixtemp_daqmm', route_name = 'campixtemp_daqmm')
	
    config.add_route('meanpixtemp_daqmm', '/meanpixtemp_daqmm')
    config.add_view('cta_project.views.meanpixtemp_daqmm', route_name = 'meanpixtemp_daqmm')	
	
    config.add_route('camclusttempmm', '/camclusttempmm')
    config.add_view('cta_project.views.camclusttempmm', route_name = 'camclusttempmm')

    config.add_route('camvcelbias_daqmm', '/camvcelbias_daqmm')
    config.add_view('cta_project.views.camvcelbias_daqmm', route_name = 'camvcelbias_daqmm')
	
    config.add_route('camlv1tempmm', '/camlv1tempmm')
    config.add_view('cta_project.views.camlv1tempmm', route_name = 'camlv1tempmm')	
	
    config.add_route('camlv2tempmm', '/camlv2tempmm')
    config.add_view('cta_project.views.camlv2tempmm', route_name = 'camlv2tempmm')	
	
    config.add_route('camlv1hummm', '/camlv1hummm')
    config.add_view('cta_project.views.camlv1hummm', route_name = 'camlv1hummm')
	
    config.add_route('camlv2hummm', '/camlv2hummm')
    config.add_view('cta_project.views.camlv2hummm', route_name = 'camlv2hummm')	
	
    config.add_route('camcoolfcptopleftmm', '/camcoolfcptopleftmm')
    config.add_view('cta_project.views.camcoolfcptopleftmm', route_name = 'camcoolfcptopleftmm')
	
    config.add_route('camcoolfcpbottrightmm', '/camcoolfcpbottrightmm')
    config.add_view('cta_project.views.camcoolfcpbottrightmm', route_name = 'camcoolfcpbottrightmm')
	
    config.add_route('camcoolrcptopleftmm', '/camcoolrcptopleftmm')
    config.add_view('cta_project.views.camcoolrcptopleftmm', route_name = 'camcoolrcptopleftmm')	
	
    config.add_route('camcoolrcpbottrightmm', '/camcoolrcpbottrightmm')
    config.add_view('cta_project.views.camcoolrcpbottrightmm', route_name = 'camcoolrcpbottrightmm')

    config.add_route('camcoolchasiastopleftmm', '/camcoolchasiastopleftmm')
    config.add_view('cta_project.views.camcoolchasiastopleftmm', route_name = 'camcoolchasiastopleftmm')
	
    config.add_route('camcoolchasiasbottrightmm', '/camcoolchasiasbottrightmm')
    config.add_view('cta_project.views.camcoolchasiasbottrightmm', route_name = 'camcoolchasiasbottrightmm')	
	
    config.add_route('camcoolchasiasftopleftmm', '/camcoolchasiasftopleftmm')
    config.add_view('cta_project.views.camcoolchasiasftopleftmm', route_name = 'camcoolchasiasftopleftmm')	
	
    config.add_route('camcoolchasiasfbottrightmm', '/camcoolchasiasfbottrightmm')
    config.add_view('cta_project.views.camcoolchasiasfbottrightmm', route_name = 'camcoolchasiasfbottrightmm')
	
    config.add_route('camcoolrearbottleftmm', '/camcoolrearbottleftmm')
    config.add_view('cta_project.views.camcoolrearbottleftmm', route_name = 'camcoolrearbottleftmm')	
	
    config.add_route('camcoolreartopleftmm', '/camcoolreartopleftmm')
    config.add_view('cta_project.views.camcoolreartopleftmm', route_name = 'camcoolreartopleftmm')
	
    config.add_route('camcoolfrontbottrightmm', '/camcoolfrontbottrightmm')
    config.add_view('cta_project.views.camcoolfrontbottrightmm', route_name = 'camcoolfrontbottrightmm')
	
    config.add_route('camcoolfronttoprightmm', '/camcoolfronttoprightmm')
    config.add_view('cta_project.views.camcoolfronttoprightmm', route_name = 'camcoolfronttoprightmm')	
	
    config.add_route('amcerrmm', '/amcerrmm')
    config.add_view('cta_project.views.amcerrmm', route_name = 'amcerrmm')

    config.add_route('l1tmm', '/l1tmm')
    config.add_view('cta_project.views.l1tmm', route_name = 'l1tmm')
	
    config.add_route('l2tmm', '/l2tmm')
    config.add_view('cta_project.views.l2tmm', route_name = 'l2tmm')	
	
    config.add_route('l2t_daqmm', '/l2t_daqmm')
    config.add_view('cta_project.views.l2t_daqmm', route_name = 'l2t_daqmm')	
	
    config.add_route('sumt_globrmm', '/sumt_globrmm')
    config.add_view('cta_project.views.sumt_globrmm', route_name = 'sumt_globrmm')
	
    config.add_route('sumt_l3mm', '/sumt_l3mm')
    config.add_view('cta_project.views.sumt_l3mm', route_name = 'sumt_l3mm')	
	
    config.add_route('sumt_dtwmm', '/sumt_dtwmm')
    config.add_view('cta_project.views.sumt_dtwmm', route_name = 'sumt_dtwmm')
	
    config.add_route('sumt_cbt1mm', '/sumt_cbt1mm')
    config.add_view('cta_project.views.sumt_cbt1mm', route_name = 'sumt_cbt1mm')
	
    config.add_route('sumt_cbt2mm', '/sumt_cbt2mm')
    config.add_view('cta_project.views.sumt_cbt2mm', route_name = 'sumt_cbt2mm')	
	
    config.add_route('sumt_acmm', '/sumt_acmm')
    config.add_view('cta_project.views.sumt_acmm', route_name = 'sumt_acmm')
	
    config.add_route('sumt_astrobmm', '/sumt_astrobmm')
    config.add_view('cta_project.views.sumt_astrobmm', route_name = 'sumt_astrobmm')
	
    config.add_route('cool_cratemm', '/cool_cratemm')
    config.add_view('cta_project.views.cool_cratemm', route_name = 'cool_cratemm')	
	
    config.add_route('cool_rackmm', '/cool_rackmm')
    config.add_view('cta_project.views.cool_rackmm', route_name = 'cool_rackmm')	
	
    config.add_route('calbtemp1mm', '/calbtemp1mm')
    config.add_view('cta_project.views.calbtemp1mm', route_name = 'calbtemp1mm')
	
    config.add_route('calbtemp2mm', '/calbtemp2mm')
    config.add_view('cta_project.views.calbtemp2mm', route_name = 'calbtemp2mm')	
	
    config.add_route('calbhummm', '/calbhummm')
    config.add_view('cta_project.views.calbhummm', route_name = 'calbhummm')
	
    config.add_route('sg_devazmm', '/sg_devazmm')
    config.add_view('cta_project.views.sg_devazmm', route_name = 'sg_devazmm')
	
    config.add_route('sg_devzdmm', '/sg_devzdmm')
    config.add_view('cta_project.views.sg_devzdmm', route_name = 'sg_devzdmm')	
	
    config.add_route('sg_camcxmm', '/sg_camcxmm')
    config.add_view('cta_project.views.sg_camcxmm', route_name = 'sg_camcxmm')

    config.add_route('sg_camcymm', '/sg_camcymm')
    config.add_view('cta_project.views.sg_camcymm', route_name = 'sg_camcymm')
	
    config.add_route('sg_starsmm', '/sg_starsmm')
    config.add_view('cta_project.views.sg_starsmm', route_name = 'sg_starsmm')	
	
    config.add_route('sg_brightmm', '/sg_brightmm')
    config.add_view('cta_project.views.sg_brightmm', route_name = 'sg_brightmm')	
	
    config.add_route('wea_tempmm', '/wea_tempmm')
    config.add_view('cta_project.views.wea_tempmm', route_name = 'wea_tempmm')
	
    config.add_route('pyro_cloudmm', '/pyro_cloudmm')
    config.add_view('cta_project.views.pyro_cloudmm', route_name = 'pyro_cloudmm')	
	
    config.add_route('pyro_skytmm', '/pyro_skytmm')
    config.add_view('cta_project.views.pyro_skytmm', route_name = 'pyro_skytmm')
	
    config.add_route('las_trans3kmmm', '/las_trans3kmmm')
    config.add_view('cta_project.views.las_trans3kmmm', route_name = 'las_trans3kmmm')
	
    config.add_route('las_trans6kmmm', '/las_trans6kmmm')
    config.add_view('cta_project.views.las_trans6kmmm', route_name = 'las_trans6kmmm')	
	
    config.add_route('las_trans9kmmm', '/las_trans9kmmm')
    config.add_view('cta_project.views.las_trans9kmmm', route_name = 'las_trans9kmmm')
	
    config.add_route('las_trans12kmmm', '/las_trans12kmmm')
    config.add_view('cta_project.views.las_trans12kmmm', route_name = 'las_trans12kmmm')
	
    config.add_route('muon_psfmm', '/muon_psfmm')
    config.add_view('cta_project.views.muon_psfmm', route_name = 'muon_psfmm')	
	
    config.add_route('muon_psfnmm', '/muon_psfnmm')
    config.add_view('cta_project.views.muon_psfnmm', route_name = 'muon_psfnmm')	
	
    config.add_route('muon_sizemm', '/muon_sizemm')
    config.add_view('cta_project.views.muon_sizemm', route_name = 'muon_sizemm')
	
    config.add_route('sbigpsf_bmm', '/sbigpsf_bmm')
    config.add_view('cta_project.views.sbigpsf_bmm', route_name = 'sbigpsf_bmm')	
	
    config.add_route('sbigpsf_lmm', '/sbigpsf_lmm')
    config.add_view('cta_project.views.sbigpsf_lmm', route_name = 'sbigpsf_lmm')
	
    config.add_route('bias_sigmm', '/bias_sigmm')
    config.add_view('cta_project.views.bias_sigmm', route_name = 'bias_sigmm')	
	
    config.add_route('hitfrac_sigmm', '/hitfrac_sigmm')
    config.add_view('cta_project.views.hitfrac_sigmm', route_name = 'hitfrac_sigmm')
	
    config.add_route('arrtm_calmm', '/arrtm_calmm')
    config.add_view('cta_project.views.arrtm_calmm', route_name = 'arrtm_calmm')	
	
    config.add_route('arrtm_intmm', '/arrtm_intmm')
    config.add_view('cta_project.views.arrtm_intmm', route_name = 'arrtm_intmm')
	
    config.add_route('arrtm_sigmm', '/arrtm_sigmm')
    config.add_view('cta_project.views.arrtm_sigmm', route_name = 'arrtm_sigmm')
	
    config.add_route('arrtmrms_calmm', '/arrtmrms_calmm')
    config.add_view('cta_project.views.arrtmrms_calmm', route_name = 'arrtmrms_calmm')	
	
    config.add_route('arrtmrms_intmm', '/arrtmrms_intmm')
    config.add_view('cta_project.views.arrtmrms_intmm', route_name = 'arrtmrms_intmm')
	
    config.add_route('arrtmrms_sigmm', '/arrtmrms_sigmm')
    config.add_view('cta_project.views.arrtmrms_sigmm', route_name = 'arrtmrms_sigmm')
	
    config.add_route('ped_pedmm', '/ped_pedmm')
    config.add_view('cta_project.views.ped_pedmm', route_name = 'ped_pedmm')	
	
    config.add_route('ped_intmm', '/ped_intmm')
    config.add_view('cta_project.views.ped_intmm', route_name = 'ped_intmm')	
	
    config.add_route('npe_intmm', '/npe_intmm')
    config.add_view('cta_project.views.npe_intmm', route_name = 'npe_intmm')
	
    config.add_route('pedrms_pedmm', '/pedrms_pedmm')
    config.add_view('cta_project.views.pedrms_pedmm', route_name = 'pedrms_pedmm')	
	
    config.add_route('pedrms_intmm', '/pedrms_intmm')
    config.add_view('cta_project.views.pedrms_intmm', route_name = 'pedrms_intmm')

    config.add_route('cfact_intmm', '/cfact_intmm')
    config.add_view('cta_project.views.cfact_intmm', route_name = 'cfact_intmm')
    config.add_route('wea_wsymm', '/wea_wsymm')	
    config.add_view('cta_project.views.wea_wsymm', route_name = 'wea_wsymm')
    config.add_route('wea_humymm', '/wea_humymm')
    config.add_view('cta_project.views.wea_humymm', route_name = 'wea_humymm')
    config.add_route('wea_gustymm', '/wea_gustymm')
    config.add_view('cta_project.views.wea_gustymm', route_name = 'wea_gustymm')
	
    config.add_route('wea_seeymm', '/wea_seeymm')
    config.add_view('cta_project.views.wea_seeymm', route_name = 'wea_seeymm')
	
    config.add_route('wea_dustymm', '/wea_dustymm')
    config.add_view('cta_project.views.wea_dustymm', route_name = 'wea_dustymm')	
	
    config.add_route('rec_tempymm', '/rec_tempymm')
    config.add_view('cta_project.views.rec_tempymm', route_name = 'rec_tempymm')	
	
    config.add_route('camtd_daqymm', '/camtd_daqymm')
    config.add_view('cta_project.views.camtd_daqymm', route_name = 'camtd_daqymm')
	
    config.add_route('camipr_daqymm', '/camipr_daqymm')
    config.add_view('cta_project.views.camipr_daqymm', route_name = 'camipr_daqymm')	
	
    config.add_route('camiprerr_daqymm', '/camiprerr_daqymm')
    config.add_view('cta_project.views.camiprerr_daqymm', route_name = 'camiprerr_daqymm')
	
    config.add_route('calq_calymm', '/calq_calymm')
    config.add_view('cta_project.views.calq_calymm', route_name = 'calq_calymm')
	
    config.add_route('calq_intymm', '/calq_intymm')
    config.add_view('cta_project.views.calq_intymm', route_name = 'calq_intymm')	
	
    config.add_route('calq_sigymm', '/calq_sigymm')
    config.add_view('cta_project.views.calq_sigymm', route_name = 'calq_sigymm')

    config.add_route('drvzdymm', '/drvzdymm')
    config.add_view('cta_project.views.drvzdymm', route_name = 'drvzdymm')
	
    config.add_route('drvdev_daqymm', '/drvdev_daqymm')
    config.add_view('cta_project.views.drvdev_daqymm', route_name = 'drvdev_daqymm')	
	
    config.add_route('camhv_daqymm', '/camhv_daqymm')
    config.add_view('cta_project.views.camhv_daqymm', route_name = 'camhv_daqymm')	
	
    config.add_route('camdc_daqymm', '/camdc_daqymm')
    config.add_view('cta_project.views.camdc_daqymm', route_name = 'camdc_daqymm')
	
    config.add_route('camdt_daqymm', '/camdt_daqymm')
    config.add_view('cta_project.views.camdt_daqymm', route_name = 'camdt_daqymm')	
	
    config.add_route('campd_daqymm', '/campd_daqymm')
    config.add_view('cta_project.views.campd_daqymm', route_name = 'campd_daqymm')
	
    config.add_route('campixtemp_daqymm', '/campixtemp_daqymm')
    config.add_view('cta_project.views.campixtemp_daqymm', route_name = 'campixtemp_daqymm')
	
    config.add_route('meanpixtemp_daqymm', '/meanpixtemp_daqymm')
    config.add_view('cta_project.views.meanpixtemp_daqymm', route_name = 'meanpixtemp_daqymm')	
	
    config.add_route('camclusttempymm', '/camclusttempymm')
    config.add_view('cta_project.views.camclusttempymm', route_name = 'camclusttempymm')

    config.add_route('camvcelbias_daqymm', '/camvcelbias_daqymm')
    config.add_view('cta_project.views.camvcelbias_daqymm', route_name = 'camvcelbias_daqymm')
	
    config.add_route('camlv1tempymm', '/camlv1tempymm')
    config.add_view('cta_project.views.camlv1tempymm', route_name = 'camlv1tempymm')	
	
    config.add_route('camlv2tempymm', '/camlv2tempymm')
    config.add_view('cta_project.views.camlv2tempymm', route_name = 'camlv2tempymm')	
	
    config.add_route('camlv1humymm', '/camlv1humymm')
    config.add_view('cta_project.views.camlv1humymm', route_name = 'camlv1humymm')
	
    config.add_route('camlv2humymm', '/camlv2humymm')
    config.add_view('cta_project.views.camlv2humymm', route_name = 'camlv2humymm')	
	
    config.add_route('camcoolfcptopleftymm', '/camcoolfcptopleftymm')
    config.add_view('cta_project.views.camcoolfcptopleftymm', route_name = 'camcoolfcptopleftymm')
	
    config.add_route('camcoolfcpbottrightymm', '/camcoolfcpbottrightymm')
    config.add_view('cta_project.views.camcoolfcpbottrightymm', route_name = 'camcoolfcpbottrightymm')
	
    config.add_route('camcoolrcptopleftymm', '/camcoolrcptopleftymm')
    config.add_view('cta_project.views.camcoolrcptopleftymm', route_name = 'camcoolrcptopleftymm')	
	
    config.add_route('camcoolrcpbottrightymm', '/camcoolrcpbottrightymm')
    config.add_view('cta_project.views.camcoolrcpbottrightymm', route_name = 'camcoolrcpbottrightymm')

    config.add_route('camcoolchasiastopleftymm', '/camcoolchasiastopleftymm')
    config.add_view('cta_project.views.camcoolchasiastopleftymm', route_name = 'camcoolchasiastopleftymm')
	
    config.add_route('camcoolchasiasbottrightymm', '/camcoolchasiasbottrightymm')
    config.add_view('cta_project.views.camcoolchasiasbottrightymm', route_name = 'camcoolchasiasbottrightymm')	
	
    config.add_route('camcoolchasiasftopleftymm', '/camcoolchasiasftopleftymm')
    config.add_view('cta_project.views.camcoolchasiasftopleftymm', route_name = 'camcoolchasiasftopleftymm')	
	
    config.add_route('camcoolchasiasfbottrightymm', '/camcoolchasiasfbottrightymm')
    config.add_view('cta_project.views.camcoolchasiasfbottrightymm', route_name = 'camcoolchasiasfbottrightymm')
	
    config.add_route('camcoolrearbottleftymm', '/camcoolrearbottleftymm')
    config.add_view('cta_project.views.camcoolrearbottleftymm', route_name = 'camcoolrearbottleftymm')	
	
    config.add_route('camcoolreartopleftymm', '/camcoolreartopleftymm')
    config.add_view('cta_project.views.camcoolreartopleftymm', route_name = 'camcoolreartopleftymm')
	
    config.add_route('camcoolfrontbottrightymm', '/camcoolfrontbottrightymm')
    config.add_view('cta_project.views.camcoolfrontbottrightymm', route_name = 'camcoolfrontbottrightymm')
	
    config.add_route('camcoolfronttoprightymm', '/camcoolfronttoprightymm')
    config.add_view('cta_project.views.camcoolfronttoprightymm', route_name = 'camcoolfronttoprightymm')	
	
    config.add_route('amcerrymm', '/amcerrymm')
    config.add_view('cta_project.views.amcerrymm', route_name = 'amcerrymm')

    config.add_route('l1tymm', '/l1tymm')
    config.add_view('cta_project.views.l1tymm', route_name = 'l1tymm')
	
    config.add_route('l2tymm', '/l2tymm')
    config.add_view('cta_project.views.l2tymm', route_name = 'l2tymm')	
	
    config.add_route('l2t_daqymm', '/l2t_daqymm')
    config.add_view('cta_project.views.l2t_daqymm', route_name = 'l2t_daqymm')	
	
    config.add_route('sumt_globrymm', '/sumt_globrymm')
    config.add_view('cta_project.views.sumt_globrymm', route_name = 'sumt_globrymm')
	
    config.add_route('sumt_l3ymm', '/sumt_l3ymm')
    config.add_view('cta_project.views.sumt_l3ymm', route_name = 'sumt_l3ymm')	
	
    config.add_route('sumt_dtwymm', '/sumt_dtwymm')
    config.add_view('cta_project.views.sumt_dtwymm', route_name = 'sumt_dtwymm')
	
    config.add_route('sumt_cbt1ymm', '/sumt_cbt1ymm')
    config.add_view('cta_project.views.sumt_cbt1ymm', route_name = 'sumt_cbt1ymm')
	
    config.add_route('sumt_cbt2ymm', '/sumt_cbt2ymm')
    config.add_view('cta_project.views.sumt_cbt2ymm', route_name = 'sumt_cbt2ymm')	
	
    config.add_route('sumt_acymm', '/sumt_acymm')
    config.add_view('cta_project.views.sumt_acymm', route_name = 'sumt_acymm')
	
    config.add_route('sumt_astrobymm', '/sumt_astrobymm')
    config.add_view('cta_project.views.sumt_astrobymm', route_name = 'sumt_astrobymm')
	
    config.add_route('cool_crateymm', '/cool_crateymm')
    config.add_view('cta_project.views.cool_crateymm', route_name = 'cool_crateymm')	
	
    config.add_route('cool_rackymm', '/cool_rackymm')
    config.add_view('cta_project.views.cool_rackymm', route_name = 'cool_rackymm')	
	
    config.add_route('calbtemp1ymm', '/calbtemp1ymm')
    config.add_view('cta_project.views.calbtemp1ymm', route_name = 'calbtemp1ymm')
	
    config.add_route('calbtemp2ymm', '/calbtemp2ymm')
    config.add_view('cta_project.views.calbtemp2ymm', route_name = 'calbtemp2ymm')	
	
    config.add_route('calbhumymm', '/calbhumymm')
    config.add_view('cta_project.views.calbhumymm', route_name = 'calbhumymm')
	
    config.add_route('sg_devazymm', '/sg_devazymm')
    config.add_view('cta_project.views.sg_devazymm', route_name = 'sg_devazymm')
	
    config.add_route('sg_devzdymm', '/sg_devzdymm')
    config.add_view('cta_project.views.sg_devzdymm', route_name = 'sg_devzdymm')	
	
    config.add_route('sg_camcxymm', '/sg_camcxymm')
    config.add_view('cta_project.views.sg_camcxymm', route_name = 'sg_camcxymm')

    config.add_route('sg_camcyymm', '/sg_camcyymm')
    config.add_view('cta_project.views.sg_camcyymm', route_name = 'sg_camcyymm')
	
    config.add_route('sg_starsymm', '/sg_starsymm')
    config.add_view('cta_project.views.sg_starsymm', route_name = 'sg_starsymm')	
	
    config.add_route('sg_brightymm', '/sg_brightymm')
    config.add_view('cta_project.views.sg_brightymm', route_name = 'sg_brightymm')	
	
    config.add_route('wea_tempymm', '/wea_tempymm')
    config.add_view('cta_project.views.wea_tempymm', route_name = 'wea_tempymm')
	
    config.add_route('pyro_cloudymm', '/pyro_cloudymm')
    config.add_view('cta_project.views.pyro_cloudymm', route_name = 'pyro_cloudymm')	
	
    config.add_route('pyro_skytymm', '/pyro_skytymm')
    config.add_view('cta_project.views.pyro_skytymm', route_name = 'pyro_skytymm')
	
    config.add_route('las_trans3kmymm', '/las_trans3kmymm')
    config.add_view('cta_project.views.las_trans3kmymm', route_name = 'las_trans3kmymm')
	
    config.add_route('las_trans6kmymm', '/las_trans6kmymm')
    config.add_view('cta_project.views.las_trans6kmymm', route_name = 'las_trans6kmymm')	
	
    config.add_route('las_trans9kmymm', '/las_trans9kmymm')
    config.add_view('cta_project.views.las_trans9kmymm', route_name = 'las_trans9kmymm')
	
    config.add_route('las_trans12kmymm', '/las_trans12kmymm')
    config.add_view('cta_project.views.las_trans12kmymm', route_name = 'las_trans12kmymm')
	
    config.add_route('muon_psfymm', '/muon_psfymm')
    config.add_view('cta_project.views.muon_psfymm', route_name = 'muon_psfymm')	
	
    config.add_route('muon_psfnymm', '/muon_psfnymm')
    config.add_view('cta_project.views.muon_psfnymm', route_name = 'muon_psfnymm')	
	
    config.add_route('muon_sizeymm', '/muon_sizeymm')
    config.add_view('cta_project.views.muon_sizeymm', route_name = 'muon_sizeymm')
	
    config.add_route('sbigpsf_bymm', '/sbigpsf_bymm')
    config.add_view('cta_project.views.sbigpsf_bymm', route_name = 'sbigpsf_bymm')	
	
    config.add_route('sbigpsf_lymm', '/sbigpsf_lymm')
    config.add_view('cta_project.views.sbigpsf_lymm', route_name = 'sbigpsf_lymm')
	
    config.add_route('bias_sigymm', '/bias_sigymm')
    config.add_view('cta_project.views.bias_sigymm', route_name = 'bias_sigymm')	
	
    config.add_route('hitfrac_sigymm', '/hitfrac_sigymm')
    config.add_view('cta_project.views.hitfrac_sigymm', route_name = 'hitfrac_sigymm')
	
    config.add_route('arrtm_calymm', '/arrtm_calymm')
    config.add_view('cta_project.views.arrtm_calymm', route_name = 'arrtm_calymm')	
	
    config.add_route('arrtm_intymm', '/arrtm_intymm')
    config.add_view('cta_project.views.arrtm_intymm', route_name = 'arrtm_intymm')
	
    config.add_route('arrtm_sigymm', '/arrtm_sigymm')
    config.add_view('cta_project.views.arrtm_sigymm', route_name = 'arrtm_sigymm')
	
    config.add_route('arrtmrms_calymm', '/arrtmrms_calymm')
    config.add_view('cta_project.views.arrtmrms_calymm', route_name = 'arrtmrms_calymm')	
	
    config.add_route('arrtmrms_intymm', '/arrtmrms_intymm')
    config.add_view('cta_project.views.arrtmrms_intymm', route_name = 'arrtmrms_intymm')
	
    config.add_route('arrtmrms_sigymm', '/arrtmrms_sigymm')
    config.add_view('cta_project.views.arrtmrms_sigymm', route_name = 'arrtmrms_sigymm')
	
    config.add_route('ped_pedymm', '/ped_pedymm')
    config.add_view('cta_project.views.ped_pedymm', route_name = 'ped_pedymm')	
	
    config.add_route('ped_intymm', '/ped_intymm')
    config.add_view('cta_project.views.ped_intymm', route_name = 'ped_intymm')	
	
    config.add_route('npe_intymm', '/npe_intymm')
    config.add_view('cta_project.views.npe_intymm', route_name = 'npe_intymm')
	
    config.add_route('pedrms_pedymm', '/pedrms_pedymm')
    config.add_view('cta_project.views.pedrms_pedymm', route_name = 'pedrms_pedymm')	
	
    config.add_route('pedrms_intymm', '/pedrms_intymm')
    config.add_view('cta_project.views.pedrms_intymm', route_name = 'pedrms_intymm')

    config.add_route('cfact_intymm', '/cfact_intymm')
    config.add_view('cta_project.views.cfact_intymm', route_name = 'cfact_intymm')
    config.add_route('wea_wsM2mm', '/wea_wsM2mm')
    config.add_view('cta_project.views.wea_wsM2mm', route_name = 'wea_wsM2mm')
    config.add_route('wea_humM2mm', '/wea_humM2M2mm')
    config.add_view('cta_project.views.wea_humM2mm', route_name = 'wea_humM2mm')
    config.add_route('wea_gustM2mm', '/wea_gustM2mm')
    config.add_view('cta_project.views.wea_gustM2mm', route_name = 'wea_gustM2mm')
	
    config.add_route('wea_seeM2mm', '/wea_seeM2mm')
    config.add_view('cta_project.views.wea_seeM2mm', route_name = 'wea_seeM2mm')
	
    config.add_route('wea_dustM2mm', '/wea_dustM2mm')
    config.add_view('cta_project.views.wea_dustM2mm', route_name = 'wea_dustM2mm')	
	
    config.add_route('rec_tempM2mm', '/rec_tempM2mm')
    config.add_view('cta_project.views.rec_tempM2mm', route_name = 'rec_tempM2mm')	
	
    config.add_route('camtd_daqM2mm', '/camtd_daqM2mm')
    config.add_view('cta_project.views.camtd_daqM2mm', route_name = 'camtd_daqM2mm')
	
    config.add_route('camipr_daqM2mm', '/camipr_daqM2mm')
    config.add_view('cta_project.views.camipr_daqM2mm', route_name = 'camipr_daqM2mm')	
	
    config.add_route('camiprerr_daqM2mm', '/camiprerr_daqM2mm')
    config.add_view('cta_project.views.camiprerr_daqM2mm', route_name = 'camiprerr_daqM2mm')
	
    config.add_route('calq_calM2mm', '/calq_calM2mm')
    config.add_view('cta_project.views.calq_calM2mm', route_name = 'calq_calM2mm')
	
    config.add_route('calq_intM2mm', '/calq_intM2mm')
    config.add_view('cta_project.views.calq_intM2mm', route_name = 'calq_intM2mm')	
	
    config.add_route('calq_sigM2mm', '/calq_sigM2mm')
    config.add_view('cta_project.views.calq_sigM2mm', route_name = 'calq_sigM2mm')

    config.add_route('drvzdM2mm', '/drvzdM2mm')
    config.add_view('cta_project.views.drvzdM2mm', route_name = 'drvzdM2mm')
	
    config.add_route('drvdev_daqM2mm', '/drvdev_daqM2mm')
    config.add_view('cta_project.views.drvdev_daqM2mm', route_name = 'drvdev_daqM2mm')	
	
    config.add_route('camhv_daqM2mm', '/camhv_daqM2mm')
    config.add_view('cta_project.views.camhv_daqM2mm', route_name = 'camhv_daqM2mm')	
	
    config.add_route('camdc_daqM2mm', '/camdc_daqM2mm')
    config.add_view('cta_project.views.camdc_daqM2mm', route_name = 'camdc_daqM2mm')
	
    config.add_route('camdt_daqM2mm', '/camdt_daqM2mm')
    config.add_view('cta_project.views.camdt_daqM2mm', route_name = 'camdt_daqM2mm')	
	
    config.add_route('campd_daqM2mm', '/campd_daqM2mm')
    config.add_view('cta_project.views.campd_daqM2mm', route_name = 'campd_daqM2mm')
	
    config.add_route('campixtemp_daqM2mm', '/campixtemp_daqM2mm')
    config.add_view('cta_project.views.campixtemp_daqM2mm', route_name = 'campixtemp_daqM2mm')
	
    config.add_route('meanpixtemp_daqM2mm', '/meanpixtemp_daqM2mm')
    config.add_view('cta_project.views.meanpixtemp_daqM2mm', route_name = 'meanpixtemp_daqM2mm')	
	
    config.add_route('camclusttempM2mm', '/camclusttempM2mm')
    config.add_view('cta_project.views.camclusttempM2mm', route_name = 'camclusttempM2mm')

    config.add_route('camvcelbias_daqM2mm', '/camvcelbias_daqM2mm')
    config.add_view('cta_project.views.camvcelbias_daqM2mm', route_name = 'camvcelbias_daqM2mm')
	
    config.add_route('camlv1tempM2mm', '/camlv1tempM2mm')
    config.add_view('cta_project.views.camlv1tempM2mm', route_name = 'camlv1tempM2mm')	
	
    config.add_route('camlv2tempM2mm', '/camlv2tempM2mm')
    config.add_view('cta_project.views.camlv2tempM2mm', route_name = 'camlv2tempM2mm')	
	
    config.add_route('camlv1humM2mm', '/camlv1humM2mm')
    config.add_view('cta_project.views.camlv1humM2mm', route_name = 'camlv1humM2mm')
	
    config.add_route('camlv2humM2mm', '/camlv2humM2mm')
    config.add_view('cta_project.views.camlv2humM2mm', route_name = 'camlv2humM2mm')	
	
    config.add_route('camcoolfcptopleftM2mm', '/camcoolfcptopleftM2mm')
    config.add_view('cta_project.views.camcoolfcptopleftM2mm', route_name = 'camcoolfcptopleftM2mm')
	
    config.add_route('camcoolfcpbottrightM2mm', '/camcoolfcpbottrightM2mm')
    config.add_view('cta_project.views.camcoolfcpbottrightM2mm', route_name = 'camcoolfcpbottrightM2mm')
	
    config.add_route('camcoolrcptopleftM2mm', '/camcoolrcptopleftM2mm')
    config.add_view('cta_project.views.camcoolrcptopleftM2mm', route_name = 'camcoolrcptopleftM2mm')	
	
    config.add_route('camcoolrcpbottrightM2mm', '/camcoolrcpbottrightM2mm')
    config.add_view('cta_project.views.camcoolrcpbottrightM2mm', route_name = 'camcoolrcpbottrightM2mm')

    config.add_route('camcoolchasiastopleftM2mm', '/camcoolchasiastopleftM2mm')
    config.add_view('cta_project.views.camcoolchasiastopleftM2mm', route_name = 'camcoolchasiastopleftM2mm')
	
    config.add_route('camcoolchasiasbottrightM2mm', '/camcoolchasiasbottrightM2mm')
    config.add_view('cta_project.views.camcoolchasiasbottrightM2mm', route_name = 'camcoolchasiasbottrightM2mm')	
	
    config.add_route('camcoolchasiasftopleftM2mm', '/camcoolchasiasftopleftM2mm')
    config.add_view('cta_project.views.camcoolchasiasftopleftM2mm', route_name = 'camcoolchasiasftopleftM2mm')	
	
    config.add_route('camcoolchasiasfbottrightM2mm', '/camcoolchasiasfbottrightM2mm')
    config.add_view('cta_project.views.camcoolchasiasfbottrightM2mm', route_name = 'camcoolchasiasfbottrightM2mm')
	
    config.add_route('camcoolrearbottleftM2mm', '/camcoolrearbottleftM2mm')
    config.add_view('cta_project.views.camcoolrearbottleftM2mm', route_name = 'camcoolrearbottleftM2mm')	
	
    config.add_route('camcoolreartopleftM2mm', '/camcoolreartopleftM2mm')
    config.add_view('cta_project.views.camcoolreartopleftM2mm', route_name = 'camcoolreartopleftM2mm')
	
    config.add_route('camcoolfrontbottrightM2mm', '/camcoolfrontbottrightM2mm')
    config.add_view('cta_project.views.camcoolfrontbottrightM2mm', route_name = 'camcoolfrontbottrightM2mm')
	
    config.add_route('camcoolfronttoprightM2mm', '/camcoolfronttoprightM2mm')
    config.add_view('cta_project.views.camcoolfronttoprightM2mm', route_name = 'camcoolfronttoprightM2mm')	
	
    config.add_route('amcerrM2mm', '/amcerrM2mm')
    config.add_view('cta_project.views.amcerrM2mm', route_name = 'amcerrM2mm')

    config.add_route('l1tM2mm', '/l1tM2mm')
    config.add_view('cta_project.views.l1tM2mm', route_name = 'l1tM2mm')
	
    config.add_route('l2tM2mm', '/l2tM2mm')
    config.add_view('cta_project.views.l2tM2mm', route_name = 'l2tM2mm')	
	
    config.add_route('l2t_daqM2mm', '/l2t_daqM2mm')
    config.add_view('cta_project.views.l2t_daqM2mm', route_name = 'l2t_daqM2mm')	
	
    config.add_route('sumt_globrM2mm', '/sumt_globrM2mm')
    config.add_view('cta_project.views.sumt_globrM2mm', route_name = 'sumt_globrM2mm')
	
    config.add_route('sumt_l3M2mm', '/sumt_l3M2mm')
    config.add_view('cta_project.views.sumt_l3M2mm', route_name = 'sumt_l3M2mm')	
	
    config.add_route('sumt_dtwM2mm', '/sumt_dtwM2mm')
    config.add_view('cta_project.views.sumt_dtwM2mm', route_name = 'sumt_dtwM2mm')
	
    config.add_route('sumt_cbt1M2mm', '/sumt_cbt1M2mm')
    config.add_view('cta_project.views.sumt_cbt1M2mm', route_name = 'sumt_cbt1M2mm')
	
    config.add_route('sumt_cbt2M2mm', '/sumt_cbt2M2mm')
    config.add_view('cta_project.views.sumt_cbt2M2mm', route_name = 'sumt_cbt2M2mm')	
	
    config.add_route('sumt_acM2mm', '/sumt_acM2mm')
    config.add_view('cta_project.views.sumt_acM2mm', route_name = 'sumt_acM2mm')
	
    config.add_route('sumt_astrobM2mm', '/sumt_astrobM2mm')
    config.add_view('cta_project.views.sumt_astrobM2mm', route_name = 'sumt_astrobM2mm')
	
    config.add_route('cool_crateM2mm', '/cool_crateM2mm')
    config.add_view('cta_project.views.cool_crateM2mm', route_name = 'cool_crateM2mm')	
	
    config.add_route('cool_rackM2mm', '/cool_rackM2mm')
    config.add_view('cta_project.views.cool_rackM2mm', route_name = 'cool_rackM2mm')	
	
    config.add_route('calbtemp1M2mm', '/calbtemp1M2mm')
    config.add_view('cta_project.views.calbtemp1M2mm', route_name = 'calbtemp1M2mm')
	
    config.add_route('calbtemp2M2mm', '/calbtemp2M2mm')
    config.add_view('cta_project.views.calbtemp2M2mm', route_name = 'calbtemp2M2mm')	
	
    config.add_route('calbhumM2mm', '/calbhumM2mm')
    config.add_view('cta_project.views.calbhumM2mm', route_name = 'calbhumM2mm')
	
    config.add_route('sg_devazM2mm', '/sg_devazM2mm')
    config.add_view('cta_project.views.sg_devazM2mm', route_name = 'sg_devazM2mm')
	
    config.add_route('sg_devzdM2mm', '/sg_devzdM2mm')
    config.add_view('cta_project.views.sg_devzdM2mm', route_name = 'sg_devzdM2mm')	
	
    config.add_route('sg_camcxM2mm', '/sg_camcxM2mm')
    config.add_view('cta_project.views.sg_camcxM2mm', route_name = 'sg_camcxM2mm')

    config.add_route('sg_camcyM2mm', '/sg_camcyM2mm')
    config.add_view('cta_project.views.sg_camcyM2mm', route_name = 'sg_camcyM2mm')
	
    config.add_route('sg_starsM2mm', '/sg_starsM2mm')
    config.add_view('cta_project.views.sg_starsM2mm', route_name = 'sg_starsM2mm')	
	
    config.add_route('sg_brightM2mm', '/sg_brightM2mm')
    config.add_view('cta_project.views.sg_brightM2mm', route_name = 'sg_brightM2mm')	
	
    config.add_route('wea_tempM2mm', '/wea_tempM2mm')
    config.add_view('cta_project.views.wea_tempM2mm', route_name = 'wea_tempM2mm')
	
    config.add_route('pyro_cloudM2mm', '/pyro_cloudM2mm')
    config.add_view('cta_project.views.pyro_cloudM2mm', route_name = 'pyro_cloudM2mm')	
	
    config.add_route('pyro_skytM2mm', '/pyro_skytM2mm')
    config.add_view('cta_project.views.pyro_skytM2mm', route_name = 'pyro_skytM2mm')
	
    config.add_route('las_trans3kmM2mm', '/las_trans3kmM2mm')
    config.add_view('cta_project.views.las_trans3kmM2mm', route_name = 'las_trans3kmM2mm')
	
    config.add_route('las_trans6kmM2mm', '/las_trans6kmM2mm')
    config.add_view('cta_project.views.las_trans6kmM2mm', route_name = 'las_trans6kmM2mm')	
	
    config.add_route('las_trans9kmM2mm', '/las_trans9kmM2mm')
    config.add_view('cta_project.views.las_trans9kmM2mm', route_name = 'las_trans9kmM2mm')
	
    config.add_route('las_trans12kmM2mm', '/las_trans12kmM2mm')
    config.add_view('cta_project.views.las_trans12kmM2mm', route_name = 'las_trans12kmM2mm')
	
    config.add_route('muon_psfM2mm', '/muon_psfM2mm')
    config.add_view('cta_project.views.muon_psfM2mm', route_name = 'muon_psfM2mm')	
	
    config.add_route('muon_psfnM2mm', '/muon_psfnM2mm')
    config.add_view('cta_project.views.muon_psfnM2mm', route_name = 'muon_psfnM2mm')	
	
    config.add_route('muon_sizeM2mm', '/muon_sizeM2mm')
    config.add_view('cta_project.views.muon_sizeM2mm', route_name = 'muon_sizeM2mm')
	
    config.add_route('sbigpsf_bM2mm', '/sbigpsf_bM2mm')
    config.add_view('cta_project.views.sbigpsf_bM2mm', route_name = 'sbigpsf_bM2mm')	
	
    config.add_route('sbigpsf_lM2mm', '/sbigpsf_lM2mm')
    config.add_view('cta_project.views.sbigpsf_lM2mm', route_name = 'sbigpsf_lM2mm')
	
    config.add_route('bias_sigM2mm', '/bias_sigM2mm')
    config.add_view('cta_project.views.bias_sigM2mm', route_name = 'bias_sigM2mm')	
	
    config.add_route('hitfrac_sigM2mm', '/hitfrac_sigM2mm')
    config.add_view('cta_project.views.hitfrac_sigM2mm', route_name = 'hitfrac_sigM2mm')
	
    config.add_route('arrtm_calM2mm', '/arrtm_calM2mm')
    config.add_view('cta_project.views.arrtm_calM2mm', route_name = 'arrtm_calM2mm')	
	
    config.add_route('arrtm_intM2mm', '/arrtm_intM2mm')
    config.add_view('cta_project.views.arrtm_intM2mm', route_name = 'arrtm_intM2mm')
	
    config.add_route('arrtm_sigM2mm', '/arrtm_sigM2mm')
    config.add_view('cta_project.views.arrtm_sigM2mm', route_name = 'arrtm_sigM2mm')
	
    config.add_route('arrtmrms_calM2mm', '/arrtmrms_calM2mm')
    config.add_view('cta_project.views.arrtmrms_calM2mm', route_name = 'arrtmrms_calM2mm')	
	
    config.add_route('arrtmrms_intM2mm', '/arrtmrms_intM2mm')
    config.add_view('cta_project.views.arrtmrms_intM2mm', route_name = 'arrtmrms_intM2mm')
	
    config.add_route('arrtmrms_sigM2mm', '/arrtmrms_sigM2mm')
    config.add_view('cta_project.views.arrtmrms_sigM2mm', route_name = 'arrtmrms_sigM2mm')
	
    config.add_route('ped_pedM2mm', '/ped_pedM2mm')
    config.add_view('cta_project.views.ped_pedM2mm', route_name = 'ped_pedM2mm')	
	
    config.add_route('ped_intM2mm', '/ped_intM2mm')
    config.add_view('cta_project.views.ped_intM2mm', route_name = 'ped_intM2mm')	
	
    config.add_route('npe_intM2mm', '/npe_intM2mm')
    config.add_view('cta_project.views.npe_intM2mm', route_name = 'npe_intM2mm')
	
    config.add_route('pedrms_pedM2mm', '/pedrms_pedM2mm')
    config.add_view('cta_project.views.pedrms_pedM2mm', route_name = 'pedrms_pedM2mm')	
	
    config.add_route('pedrms_intM2mm', '/pedrms_intM2mm')
    config.add_view('cta_project.views.pedrms_intM2mm', route_name = 'pedrms_intM2mm')

    config.add_route('cfact_intM2mm', '/cfact_intM2mm')
    config.add_view('cta_project.views.cfact_intM2mm', route_name = 'cfact_intM2mm')
    config.add_route('wea_wsyM2mm', '/wea_wsyM2mm')	
    config.add_view('cta_project.views.wea_wsyM2mm', route_name = 'wea_wsyM2mm')
    config.add_route('wea_humyM2mm', '/wea_humyM2mm')
    config.add_view('cta_project.views.wea_humyM2mm', route_name = 'wea_humyM2mm')
    config.add_route('wea_gustyM2mm', '/wea_gustyM2mm')
    config.add_view('cta_project.views.wea_gustyM2mm', route_name = 'wea_gustyM2mm')
	
    config.add_route('wea_seeyM2mm', '/wea_seeyM2mm')
    config.add_view('cta_project.views.wea_seeyM2mm', route_name = 'wea_seeyM2mm')
	
    config.add_route('wea_dustyM2mm', '/wea_dustyM2mm')
    config.add_view('cta_project.views.wea_dustyM2mm', route_name = 'wea_dustyM2mm')	
	
    config.add_route('rec_tempyM2mm', '/rec_tempyM2mm')
    config.add_view('cta_project.views.rec_tempyM2mm', route_name = 'rec_tempyM2mm')	
	
    config.add_route('camtd_daqyM2mm', '/camtd_daqyM2mm')
    config.add_view('cta_project.views.camtd_daqyM2mm', route_name = 'camtd_daqyM2mm')
	
    config.add_route('camipr_daqyM2mm', '/camipr_daqyM2mm')
    config.add_view('cta_project.views.camipr_daqyM2mm', route_name = 'camipr_daqyM2mm')	
	
    config.add_route('camiprerr_daqyM2mm', '/camiprerr_daqyM2mm')
    config.add_view('cta_project.views.camiprerr_daqyM2mm', route_name = 'camiprerr_daqyM2mm')
	
    config.add_route('calq_calyM2mm', '/calq_calyM2mm')
    config.add_view('cta_project.views.calq_calyM2mm', route_name = 'calq_calyM2mm')
	
    config.add_route('calq_intyM2mm', '/calq_intyM2mm')
    config.add_view('cta_project.views.calq_intyM2mm', route_name = 'calq_intyM2mm')	
	
    config.add_route('calq_sigyM2mm', '/calq_sigyM2mm')
    config.add_view('cta_project.views.calq_sigyM2mm', route_name = 'calq_sigyM2mm')

    config.add_route('drvzdyM2mm', '/drvzdyM2mm')
    config.add_view('cta_project.views.drvzdyM2mm', route_name = 'drvzdyM2mm')
	
    config.add_route('drvdev_daqyM2mm', '/drvdev_daqyM2mm')
    config.add_view('cta_project.views.drvdev_daqyM2mm', route_name = 'drvdev_daqyM2mm')	
	
    config.add_route('camhv_daqyM2mm', '/camhv_daqyM2mm')
    config.add_view('cta_project.views.camhv_daqyM2mm', route_name = 'camhv_daqyM2mm')	
	
    config.add_route('camdc_daqyM2mm', '/camdc_daqyM2mm')
    config.add_view('cta_project.views.camdc_daqyM2mm', route_name = 'camdc_daqyM2mm')
	
    config.add_route('camdt_daqyM2mm', '/camdt_daqyM2mm')
    config.add_view('cta_project.views.camdt_daqyM2mm', route_name = 'camdt_daqyM2mm')	
	
    config.add_route('campd_daqyM2mm', '/campd_daqyM2mm')
    config.add_view('cta_project.views.campd_daqyM2mm', route_name = 'campd_daqyM2mm')
	
    config.add_route('campixtemp_daqyM2mm', '/campixtemp_daqyM2mm')
    config.add_view('cta_project.views.campixtemp_daqyM2mm', route_name = 'campixtemp_daqyM2mm')
	
    config.add_route('meanpixtemp_daqyM2mm', '/meanpixtemp_daqyM2mm')
    config.add_view('cta_project.views.meanpixtemp_daqyM2mm', route_name = 'meanpixtemp_daqyM2mm')	
	
    config.add_route('camclusttempyM2mm', '/camclusttempyM2mm')
    config.add_view('cta_project.views.camclusttempyM2mm', route_name = 'camclusttempyM2mm')

    config.add_route('camvcelbias_daqyM2mm', '/camvcelbias_daqyM2mm')
    config.add_view('cta_project.views.camvcelbias_daqyM2mm', route_name = 'camvcelbias_daqyM2mm')
	
    config.add_route('camlv1tempyM2mm', '/camlv1tempyM2mm')
    config.add_view('cta_project.views.camlv1tempyM2mm', route_name = 'camlv1tempyM2mm')	
	
    config.add_route('camlv2tempyM2mm', '/camlv2tempyM2mm')
    config.add_view('cta_project.views.camlv2tempyM2mm', route_name = 'camlv2tempyM2mm')	
	
    config.add_route('camlv1humyM2mm', '/camlv1humyM2mm')
    config.add_view('cta_project.views.camlv1humyM2mm', route_name = 'camlv1humyM2mm')
	
    config.add_route('camlv2humyM2mm', '/camlv2humyM2mm')
    config.add_view('cta_project.views.camlv2humyM2mm', route_name = 'camlv2humyM2mm')	
	
    config.add_route('camcoolfcptopleftyM2mm', '/camcoolfcptopleftyM2mm')
    config.add_view('cta_project.views.camcoolfcptopleftyM2mm', route_name = 'camcoolfcptopleftyM2mm')
	
    config.add_route('camcoolfcpbottrightyM2mm', '/camcoolfcpbottrightyM2mm')
    config.add_view('cta_project.views.camcoolfcpbottrightyM2mm', route_name = 'camcoolfcpbottrightyM2mm')
	
    config.add_route('camcoolrcptopleftyM2mm', '/camcoolrcptopleftyM2mm')
    config.add_view('cta_project.views.camcoolrcptopleftyM2mm', route_name = 'camcoolrcptopleftyM2mm')	
	
    config.add_route('camcoolrcpbottrightyM2mm', '/camcoolrcpbottrightyM2mm')
    config.add_view('cta_project.views.camcoolrcpbottrightyM2mm', route_name = 'camcoolrcpbottrightyM2mm')

    config.add_route('camcoolchasiastopleftyM2mm', '/camcoolchasiastopleftyM2mm')
    config.add_view('cta_project.views.camcoolchasiastopleftyM2mm', route_name = 'camcoolchasiastopleftyM2mm')
	
    config.add_route('camcoolchasiasbottrightyM2mm', '/camcoolchasiasbottrightyM2mm')
    config.add_view('cta_project.views.camcoolchasiasbottrightyM2mm', route_name = 'camcoolchasiasbottrightyM2mm')	
	
    config.add_route('camcoolchasiasftopleftyM2mm', '/camcoolchasiasftopleftyM2mm')
    config.add_view('cta_project.views.camcoolchasiasftopleftyM2mm', route_name = 'camcoolchasiasftopleftyM2mm')	
	
    config.add_route('camcoolchasiasfbottrightyM2mm', '/camcoolchasiasfbottrightyM2mm')
    config.add_view('cta_project.views.camcoolchasiasfbottrightyM2mm', route_name = 'camcoolchasiasfbottrightyM2mm')
	
    config.add_route('camcoolrearbottleftyM2mm', '/camcoolrearbottleftyM2mm')
    config.add_view('cta_project.views.camcoolrearbottleftyM2mm', route_name = 'camcoolrearbottleftyM2mm')	
	
    config.add_route('camcoolreartopleftyM2mm', '/camcoolreartopleftyM2mm')
    config.add_view('cta_project.views.camcoolreartopleftyM2mm', route_name = 'camcoolreartopleftyM2mm')
	
    config.add_route('camcoolfrontbottrightyM2mm', '/camcoolfrontbottrightyM2mm')
    config.add_view('cta_project.views.camcoolfrontbottrightyM2mm', route_name = 'camcoolfrontbottrightyM2mm')
	
    config.add_route('camcoolfronttoprightyM2mm', '/camcoolfronttoprightyM2mm')
    config.add_view('cta_project.views.camcoolfronttoprightyM2mm', route_name = 'camcoolfronttoprightyM2mm')	
	
    config.add_route('amcerryM2mm', '/amcerryM2mm')
    config.add_view('cta_project.views.amcerryM2mm', route_name = 'amcerryM2mm')

    config.add_route('l1tyM2mm', '/l1tyM2mm')
    config.add_view('cta_project.views.l1tyM2mm', route_name = 'l1tyM2mm')
	
    config.add_route('l2tyM2mm', '/l2tyM2mm')
    config.add_view('cta_project.views.l2tyM2mm', route_name = 'l2tyM2mm')	
	
    config.add_route('l2t_daqyM2mm', '/l2t_daqyM2mm')
    config.add_view('cta_project.views.l2t_daqyM2mm', route_name = 'l2t_daqyM2mm')	
	
    config.add_route('sumt_globryM2mm', '/sumt_globryM2mm')
    config.add_view('cta_project.views.sumt_globryM2mm', route_name = 'sumt_globryM2mm')
	
    config.add_route('sumt_l3yM2mm', '/sumt_l3yM2mm')
    config.add_view('cta_project.views.sumt_l3yM2mm', route_name = 'sumt_l3yM2mm')	
	
    config.add_route('sumt_dtwyM2mm', '/sumt_dtwyM2mm')
    config.add_view('cta_project.views.sumt_dtwyM2mm', route_name = 'sumt_dtwyM2mm')
	
    config.add_route('sumt_cbt1yM2mm', '/sumt_cbt1yM2mm')
    config.add_view('cta_project.views.sumt_cbt1yM2mm', route_name = 'sumt_cbt1yM2mm')
	
    config.add_route('sumt_cbt2yM2mm', '/sumt_cbt2yM2mm')
    config.add_view('cta_project.views.sumt_cbt2yM2mm', route_name = 'sumt_cbt2yM2mm')	
	
    config.add_route('sumt_acyM2mm', '/sumt_acyM2mm')
    config.add_view('cta_project.views.sumt_acyM2mm', route_name = 'sumt_acyM2mm')
	
    config.add_route('sumt_astrobyM2mm', '/sumt_astrobyM2mm')
    config.add_view('cta_project.views.sumt_astrobyM2mm', route_name = 'sumt_astrobyM2mm')
	
    config.add_route('cool_crateyM2mm', '/cool_crateyM2mm')
    config.add_view('cta_project.views.cool_crateyM2mm', route_name = 'cool_crateyM2mm')	
	
    config.add_route('cool_rackyM2mm', '/cool_rackyM2mm')
    config.add_view('cta_project.views.cool_rackyM2mm', route_name = 'cool_rackyM2mm')	
	
    config.add_route('calbtemp1yM2mm', '/calbtemp1yM2mm')
    config.add_view('cta_project.views.calbtemp1yM2mm', route_name = 'calbtemp1yM2mm')
	
    config.add_route('calbtemp2yM2mm', '/calbtemp2yM2mm')
    config.add_view('cta_project.views.calbtemp2yM2mm', route_name = 'calbtemp2yM2mm')	
	
    config.add_route('calbhumyM2mm', '/calbhumyM2mm')
    config.add_view('cta_project.views.calbhumyM2mm', route_name = 'calbhumyM2mm')
	
    config.add_route('sg_devazyM2mm', '/sg_devazyM2mm')
    config.add_view('cta_project.views.sg_devazyM2mm', route_name = 'sg_devazyM2mm')
	
    config.add_route('sg_devzdyM2mm', '/sg_devzdyM2mm')
    config.add_view('cta_project.views.sg_devzdyM2mm', route_name = 'sg_devzdyM2mm')	
	
    config.add_route('sg_camcxyM2mm', '/sg_camcxyM2mm')
    config.add_view('cta_project.views.sg_camcxyM2mm', route_name = 'sg_camcxyM2mm')

    config.add_route('sg_camcyyM2mm', '/sg_camcyyM2mm')
    config.add_view('cta_project.views.sg_camcyyM2mm', route_name = 'sg_camcyyM2mm')
	
    config.add_route('sg_starsyM2mm', '/sg_starsyM2mm')
    config.add_view('cta_project.views.sg_starsyM2mm', route_name = 'sg_starsyM2mm')	
	
    config.add_route('sg_brightyM2mm', '/sg_brightyM2mm')
    config.add_view('cta_project.views.sg_brightyM2mm', route_name = 'sg_brightyM2mm')	
	
    config.add_route('wea_tempyM2mm', '/wea_tempyM2mm')
    config.add_view('cta_project.views.wea_tempyM2mm', route_name = 'wea_tempyM2mm')
	
    config.add_route('pyro_cloudyM2mm', '/pyro_cloudyM2mm')
    config.add_view('cta_project.views.pyro_cloudyM2mm', route_name = 'pyro_cloudyM2mm')	
	
    config.add_route('pyro_skytyM2mm', '/pyro_skytyM2mm')
    config.add_view('cta_project.views.pyro_skytyM2mm', route_name = 'pyro_skytyM2mm')
	
    config.add_route('las_trans3kmyM2mm', '/las_trans3kmyM2mm')
    config.add_view('cta_project.views.las_trans3kmyM2mm', route_name = 'las_trans3kmyM2mm')
	
    config.add_route('las_trans6kmyM2mm', '/las_trans6kmyM2mm')
    config.add_view('cta_project.views.las_trans6kmyM2mm', route_name = 'las_trans6kmyM2mm')	
	
    config.add_route('las_trans9kmyM2mm', '/las_trans9kmyM2mm')
    config.add_view('cta_project.views.las_trans9kmyM2mm', route_name = 'las_trans9kmyM2mm')
	
    config.add_route('las_trans12kmyM2mm', '/las_trans12kmyM2mm')
    config.add_view('cta_project.views.las_trans12kmyM2mm', route_name = 'las_trans12kmyM2mm')
	
    config.add_route('muon_psfyM2mm', '/muon_psfyM2mm')
    config.add_view('cta_project.views.muon_psfyM2mm', route_name = 'muon_psfyM2mm')	
	
    config.add_route('muon_psfnyM2mm', '/muon_psfnyM2mm')
    config.add_view('cta_project.views.muon_psfnyM2mm', route_name = 'muon_psfnyM2mm')	
	
    config.add_route('muon_sizeyM2mm', '/muon_sizeyM2mm')
    config.add_view('cta_project.views.muon_sizeyM2mm', route_name = 'muon_sizeyM2mm')
	
    config.add_route('sbigpsf_byM2mm', '/sbigpsf_byM2mm')
    config.add_view('cta_project.views.sbigpsf_byM2mm', route_name = 'sbigpsf_byM2mm')	
	
    config.add_route('sbigpsf_lyM2mm', '/sbigpsf_lyM2mm')
    config.add_view('cta_project.views.sbigpsf_lyM2mm', route_name = 'sbigpsf_lyM2mm')
	
    config.add_route('bias_sigyM2mm', '/bias_sigyM2mm')
    config.add_view('cta_project.views.bias_sigyM2mm', route_name = 'bias_sigyM2mm')	
	
    config.add_route('hitfrac_sigyM2mm', '/hitfrac_sigyM2mm')
    config.add_view('cta_project.views.hitfrac_sigyM2mm', route_name = 'hitfrac_sigyM2mm')
	
    config.add_route('arrtm_calyM2mm', '/arrtm_calyM2mm')
    config.add_view('cta_project.views.arrtm_calyM2mm', route_name = 'arrtm_calyM2mm')	
	
    config.add_route('arrtm_intyM2mm', '/arrtm_intyM2mm')
    config.add_view('cta_project.views.arrtm_intyM2mm', route_name = 'arrtm_intyM2mm')
	
    config.add_route('arrtm_sigyM2mm', '/arrtm_sigyM2mm')
    config.add_view('cta_project.views.arrtm_sigyM2mm', route_name = 'arrtm_sigyM2mm')
	
    config.add_route('arrtmrms_calyM2mm', '/arrtmrms_calyM2mm')
    config.add_view('cta_project.views.arrtmrms_calyM2mm', route_name = 'arrtmrms_calyM2mm')	
	
    config.add_route('arrtmrms_intyM2mm', '/arrtmrms_intyM2mm')
    config.add_view('cta_project.views.arrtmrms_intyM2mm', route_name = 'arrtmrms_intyM2mm')
	
    config.add_route('arrtmrms_sigyM2mm', '/arrtmrms_sigyM2mm')
    config.add_view('cta_project.views.arrtmrms_sigyM2mm', route_name = 'arrtmrms_sigyM2mm')
	
    config.add_route('ped_pedyM2mm', '/ped_pedyM2mm')
    config.add_view('cta_project.views.ped_pedyM2mm', route_name = 'ped_pedyM2mm')	
	
    config.add_route('ped_intyM2mm', '/ped_intyM2mm')
    config.add_view('cta_project.views.ped_intyM2mm', route_name = 'ped_intyM2mm')	
	
    config.add_route('npe_intyM2mm', '/npe_intyM2mm')
    config.add_view('cta_project.views.npe_intyM2mm', route_name = 'npe_intyM2mm')
	
    config.add_route('pedrms_pedyM2mm', '/pedrms_pedyM2mm')
    config.add_view('cta_project.views.pedrms_pedyM2mm', route_name = 'pedrms_pedyM2mm')	
	
    config.add_route('pedrms_intyM2mm', '/pedrms_intyM2mm')
    config.add_view('cta_project.views.pedrms_intyM2mm', route_name = 'pedrms_intyM2mm')

    config.add_route('cfact_intyM2mm', '/cfact_intyM2mm')
    config.add_view('cta_project.views.cfact_intyM2mm', route_name = 'cfact_intyM2mm')	
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
	
