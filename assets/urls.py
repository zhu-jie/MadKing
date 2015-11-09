
from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'report/$',views.asset_report,name='asset_report' ),
    #url(r'report/bulk_create/$',views.bulk_create_assets,name='bulk_create_assets' ),
    url(r'report/asset_with_no_asset_id/$',views.asset_with_no_asset_id,name='acquire_asset_id' ),
    url(r'^report_test/$',views.asset_report_test ),
    url(r'^acquire_asset_id_test/$',views.acquire_asset_id_test ),
    url(r'^fetch_asset_id/$',views.fetch_asset_id ),
    url(r'^new_assets/approval/$',views.new_assets_approval,name="new_assets_approval" ),
    url(r'^asset_list/$',views.asset_list,name="asset_list" ),
    url(r'^asset_list/list/$',views.get_asset_list,name="get_asset_list" ),


]
