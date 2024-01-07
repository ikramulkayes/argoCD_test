"""
URL configuration for projectname project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# projectname/urls.py
from django.contrib import admin
from django.urls import path, include
#from django.conf.urls import url
from authentication.views import ReactView, CheckEmployeeExistenceView
#from django.views.generic import RedirectView
from login_stuffs.views import ReactView_Register_admin, CheckUserExistenceView , ReactView_DeleteMember,ReactView_Edit_Field_Admin
from field_officer_login.views import ReactView_Register_Field_Officer, CheckUserExistenceView_Field_Officer,ReactView_DeleteMember_Field_Officer,ReactView_Edit_Field_Officer
from expert.views import ReactView_Register_Expert,CheckUserExistenceView_Expert,ReactView_DeleteMember_Expert,ReactView_Edit_Expert
from incoming_request.views import ReactView_DeleteMember_Incoming_request,ReactView_Register_Incoming_Request,CheckUserExistenceView_Incoming_request
from all_login_credentials.views import ReactView_DeleteMember_all_login,ReactView_Register_all_login,CheckUserExistenceView_all_login,ReactView_Edit_all_login
from bloglist.views import ReactView_DeleteMember_BlogList,ReactView_Register_BlogList_Comments,ReactView_Register_BlogList,CheckUserExistenceView_BlogList,ReactView_AddComment,ReactView_DeleteComment,ReactView_Blog_Edit,ReactView_DeleteAllComment,Search_In_BlogList
from django.conf.urls.static import static
from django.conf import settings
from blog_images.views import GetImageView, YourModelNameView
from dataforfoods.views import ReactView_Register_DataForFoods
from auction_posts_datas.views import ReactView_Register_Auction_Prodcuts,CheckPostsExistenceView_Auction_List,ReactView_DeleteMember_Auction_list,ReactView_Edit_Auction_list_current_price,ReactView_Search_Sort_Auction_Prodcuts
from auction_images.views import GetImageView_Auction,YourModelNameView_Auction
from businessmen.views import ReactView_Register_Businessmen,CheckUserExistenceView_Businessmen,ReactView_Edit_Businessmen,ReactView_DeleteMember_Businessmen
from latest_bidding.views import ReactView_Register_latest_bidding,CheckUserExistenceView_latest_bidding,ReactView_Edit_latest_bidding,ReactView_DeleteMember_latest_bidding, ReactView_Edit_latest_bidding_ended, ReactView_Edit_latest_bidding_maxprice
from incoming_auction_request.views import ReactView_Register_Incoming_Auction_Prodcuts,CheckPostsExistenceView_Incoming_Auction_List,ReactView_DeleteMember_Incoming_Auction_list,ReactView_Edit_Incoming_Auction_list_current_price
from incoming_auction_images.views import GetImageView_incoming_Auction,YourModelNameView_incoming_Auction
from farmer_credentials.views import ReactView_Register_Farmer,CheckUserExistenceView_Farmer,ReactView_Edit_Farmer,ReactView_DeleteMember_Farmer
from pending_businessmen_payment.views import ReactView_Register_pending_businessmen_payment,ReactView_DeleteMember_pending_businessmen_payment,ReactView_Search_Sort_pending_businessmen_payment,ReactView_Get_product_details
from pending_farmer_payment.views import ReactView_Register_pending_farmer_payment,ReactView_DeleteMember_pending_farmer_payment,ReactView_Search_Sort_pending_farmer_payment,ReactView_Get_pending_farmer_paymentdata
from deliverymen.views import ReactView_Register_Deliverymen,CheckUserExistenceView_Deliverymen,ReactView_Edit_Deliverymen,ReactView_DeleteMember_Deliverymen
from delivery_bountys.views import ReactView_Register_bounties, ReactView_DeleteMember_bounties,ReactView_Search_Sort_bounties
from delivery_bountys_booked.views import ReactView_Register_bounties_accepted,ReactView_DeleteMember_bounties_accepted,ReactView_Search_Sort_bounties_accepted,ReactView_UpdateDeliveryState,ReactView_GetDeliveryState
from pending_on_delivery_products.views import ReactView_Register_pending_on_delivery,ReactView_DeleteMember_pending_on_delivery,ReactView_Search_Sort_pending_on_delivery,ReactView_Get_product_details_pending_on_delivery
from farmer_wallet.views import ReactView_Register_farmer_wallet,ReactView_Search_farmer_wallet,ReactView_Update_farmer_wallet
from farmer_review.views import ReactView_Register_farmer_review,ReactView_Search_farmer_review


urlpatterns = [
    path('', ReactView.as_view(), name="anything"),
    path('admin/', admin.site.urls),
    path('check_employee/', CheckEmployeeExistenceView.as_view(), name="check_employee"),
    #path('authentication/', include('authentication.urls')),  # Include your authentication app's URLs

    #Incoming request
    path('register_incoming_request/', ReactView_Register_Incoming_Request.as_view(), name="anything"),#incoming_request register
    path('delete_incoming_request/', ReactView_DeleteMember_Incoming_request.as_view(), name="delete_member"),  #delete incoming request

    #For all Login
    path('register_all_login',ReactView_Register_all_login.as_view(), name='anything'), #for all login 
    path('login_all_login/', CheckUserExistenceView_all_login.as_view(), name="check_user"), # for  all login
    path('delete_all_login/', ReactView_DeleteMember_all_login.as_view(), name="delete_member"), 
    path('edit_all_login/', ReactView_Edit_all_login.as_view(), name="anything"), # for edit all login


    #For Admin
    path('register/', ReactView_Register_admin.as_view(), name="anything"),# for admins register
    path('login/', CheckUserExistenceView.as_view(), name="check_user"), # for  admins logins
    path('delete_admin/', ReactView_DeleteMember.as_view(), name="delete_member"), # for delete admin
    path('edit_admin/', ReactView_Edit_Field_Admin.as_view(), name="anything"), # for edit admin

    #For Field Officer
    path('register_field_officer/', ReactView_Register_Field_Officer.as_view(), name="anything"),# for field officer register
    path('login_field_officer/', CheckUserExistenceView_Field_Officer.as_view(), name="check_user"), # for  field officer logins
    path('delete_field_officer/', ReactView_DeleteMember_Field_Officer.as_view(), name="delete_field_officer"),#for delete field officer
    path('edit_field_officer/', ReactView_Edit_Field_Officer.as_view(), name="anything"), # for edit field officer

    #For Expert
    path('register_expert/', ReactView_Register_Expert.as_view(), name="anything"),# for expert register
    path('login_expert/', CheckUserExistenceView_Expert.as_view(), name="check_user"), # for  expert logins
    path('delete_expert/', ReactView_DeleteMember_Expert.as_view(), name="delete_field_officer"),#for delete expert 
    path('edit_expert/', ReactView_Edit_Expert.as_view(), name="anything"), # for edit expert

    #For Businessmen
    path('register_businessman/', ReactView_Register_Businessmen.as_view(), name="anything"),# for businessmen register
    path('login_businessman/', CheckUserExistenceView_Businessmen.as_view(), name="check_user"), # for  businessmen  logins
    path('delete_businessman/', ReactView_DeleteMember_Businessmen.as_view(), name="delete_field_officer"),#for delete businessmen 
    path('edit_businessman/', ReactView_Edit_Businessmen.as_view(), name="anything"), # for edit businessmen 

    #For Farmer
    path('register_farmer/', ReactView_Register_Farmer.as_view(), name="anything"),# for farmer register
    path('login_farmer/', CheckUserExistenceView_Farmer.as_view(), name="check_user"), # for  farmer  logins
    path('delete_farmer/', ReactView_DeleteMember_Farmer.as_view(), name="delete_field_officer"),#for delete farmer 
    path('edit_farmer/', ReactView_Edit_Farmer.as_view(), name="anything"), # for edit farmer 

    #For Deliverymen
    path('register_deliveryman/', ReactView_Register_Deliverymen.as_view(), name="anything"),# for deliveryman register
    path('login_deliveryman/', CheckUserExistenceView_Deliverymen.as_view(), name="check_user"), # for  deliveryman  logins
    path('delete_deliveryman/', ReactView_DeleteMember_Deliverymen.as_view(), name="delete_field_officer"),#for delete deliveryman 
    path('edit_deliveryman/', ReactView_Edit_Deliverymen.as_view(), name="anything"), # for edit deliveryman 

    #BLOG Part

    path('register_blog_list/', ReactView_Register_BlogList.as_view(), name="anything"),# for fetching and adding bloglist
    path('login_blog_list/', CheckUserExistenceView_BlogList.as_view(), name="check_user"), # for checking a blog exists
    path('delete_blog_list/', ReactView_DeleteMember_BlogList.as_view(), name="delete_field_officer"), # deleting blog
    path('edit_blog_list/', ReactView_Blog_Edit.as_view(), name="anything"),# for fetching and adding bloglist
    path('search_blog_list/', Search_In_BlogList.as_view(), name="anything"),# for fetching and adding bloglist

    #Blog Comment
    path('register_add_comment/', ReactView_AddComment.as_view(), name="anything"),# for adding comments
    path('register_delete_comment/', ReactView_DeleteComment.as_view(), name="anything"),# for deleting comments
    path('register_delete_all_comment/', ReactView_DeleteAllComment.as_view(), name="anything"),# for deleting comments

    #For Blog Images
    path('register_add_blog_images/', YourModelNameView.as_view(), name="anything"),# for images
    path('login_blog_images/', GetImageView.as_view(), name="check_user"), # for checking a blog image exists if exists it returns the image

    #For Data for foods
    path('register_add_dataforfoods/', ReactView_Register_DataForFoods.as_view(), name="anything"),# for adding and getting field officer data posted

    #For auction
    path('register_add_auction_products/', ReactView_Register_Auction_Prodcuts.as_view(), name="anything"), #for adding auction products
    path('check_auction_products/', CheckPostsExistenceView_Auction_List.as_view(), name="anything"), #for checking if a product exists or not
    path('delete_auction_products/', ReactView_DeleteMember_Auction_list.as_view(), name="anything"),#for delete auction products
    path('edit_auction_products_current_price/', ReactView_Edit_Auction_list_current_price.as_view(), name="anything"), # for edit acution post price
    path('search_auction_products/', ReactView_Search_Sort_Auction_Prodcuts.as_view(), name="anything"), # for search acution post price

    #For auction images
    path('register_add_auction_images/', YourModelNameView_Auction.as_view(), name="anything"),# for images
    path('login_auction_images/', GetImageView_Auction.as_view(), name="check_user"), # for checking a blog image exists if exists it returns the image
    

    #For latest bidding
    path('register_latest_bidding/', ReactView_Register_latest_bidding.as_view(), name="anything"),# for latest_bidding register
    path('login_latest_bidding/', CheckUserExistenceView_latest_bidding.as_view(), name="check_user"), # for  latest_bidding logins
    path('delete_latest_bidding/', ReactView_DeleteMember_latest_bidding.as_view(), name="delete_field_officer"),#for delete latest_bidding
    path('edit_latest_bidding/', ReactView_Edit_latest_bidding.as_view(), name="anything"), # for edit latest_bidding
    path('edit_latest_bidding_ending/', ReactView_Edit_latest_bidding_ended.as_view(), name="anything"), # for edit latest_bidding
    path('edit_latest_bidding_maxprice/', ReactView_Edit_latest_bidding_maxprice.as_view(), name="anything"), # for edit latest_bidding

    #For incoming auction request
    path('register_add_incoming_auction_products/', ReactView_Register_Incoming_Auction_Prodcuts.as_view(), name="anything"), #for adding auction products
    path('check_incoming_auction_products/', CheckPostsExistenceView_Incoming_Auction_List.as_view(), name="anything"), #for checking if a product exists or not
    path('delete_incoming_auction_products/', ReactView_DeleteMember_Incoming_Auction_list.as_view(), name="anything"),#for delete auction products
    path('edit_incoming_auction_products_current_price/', ReactView_Edit_Incoming_Auction_list_current_price.as_view(), name="anything"), # for edit acution post price

    #For incoming auction images
    path('register_add_incoming_auction_images/', YourModelNameView_incoming_Auction.as_view(), name="anything"),# for images
    path('login_incoming_auction_images/', GetImageView_incoming_Auction.as_view(), name="check_user"), # for checking a blog image exists if exists it returns the image


    #For pending businessmen payment
    path('register_pending_payment/', ReactView_Register_pending_businessmen_payment.as_view(), name="anything"),# for pending businesmen payment register
    path('delete_pending_payment/', ReactView_DeleteMember_pending_businessmen_payment.as_view(), name="delete_field_officer"),#for delete pending businesmen payment
    path('get_businessman_pending_payment/', ReactView_Search_Sort_pending_businessmen_payment.as_view(), name="anything"), # for getting  pending businesmen payment
    path('get_businessman_pending_payment_post_details/', ReactView_Get_product_details.as_view(), name="anything"), # for getting  pending businesmen product details

    #For pending farmer payment
    path('register_pending_farmer_payment/', ReactView_Register_pending_farmer_payment.as_view(), name="anything"),# for pending businesmen payment register
    path('delete_pending_farmer_payment/', ReactView_DeleteMember_pending_farmer_payment.as_view(), name="delete_field_officer"),#for delete pending businesmen payment
    path('get_pending_farmer_payment/', ReactView_Search_Sort_pending_farmer_payment.as_view(), name="anything"), # for getting  pending businesmen payment
    path('get_pending_farmer_payment_data/', ReactView_Get_pending_farmer_paymentdata.as_view(), name="anything"), # for getting  pending businesmen payment

    #For pending delivery bounties
    path('register_deilvery_bounty/', ReactView_Register_bounties.as_view(), name="anything"),# for pending delivery bounties register
    path('delete_deilvery_bounty/', ReactView_DeleteMember_bounties.as_view(), name="delete_field_officer"),#for delete pending businesmen payment
    path('get_deilvery_bounty/', ReactView_Search_Sort_bounties.as_view(), name="anything"), # for getting  pending businesmen payment  


    #For pending delivery bounties accepted
    path('register_deilvery_bounty_booked/', ReactView_Register_bounties_accepted.as_view(), name="anything"),# for pending delivery bounties accepted register
    path('delete_deilvery_bounty_booked/', ReactView_DeleteMember_bounties_accepted.as_view(), name="delete_field_officer"),#for delete pending delivery bounties accepted
    path('get_deilvery_bounty_booked/', ReactView_Search_Sort_bounties_accepted.as_view(), name="anything"), # for getting  pending delivery bounties accepted  
    path('get_deilvery_bounty_booked_delivery_state_update/', ReactView_UpdateDeliveryState.as_view(), name="anything"), # for getting  pending delivery bounties accepted
    path('get_deilvery_bounty_booked_delivery_state_check/', ReactView_GetDeliveryState.as_view(), name="anything"), # for getting  pending delivery bounties accepted

    #For pending on delivery products list
    path('register_pending_delivery_products/', ReactView_Register_pending_on_delivery.as_view(), name="anything"),# for pending businesmen payment register
    path('delete_pending_delivery_products/', ReactView_DeleteMember_pending_on_delivery.as_view(), name="delete_field_officer"),#for delete pending businesmen payment
    path('get_pending_delivery_products/', ReactView_Search_Sort_pending_on_delivery.as_view(), name="anything"), # for getting  pending businesmen payment
    path('get_pending_delivery_products_post_details/', ReactView_Get_product_details_pending_on_delivery.as_view(), name="anything"), # for getting  pending businesmen product details

    #For farmer wallet
    path('register_farmer_wallet/', ReactView_Register_farmer_wallet.as_view(), name="anything"),# for pending businesmen payment register
    path('get_farmer_wallet/', ReactView_Search_farmer_wallet.as_view(), name="anything"),#for get pending businesmen payment
    path('update_farmer_wallet/', ReactView_Update_farmer_wallet.as_view(), name="anything"),#for get pending businesmen payment   

    #For farmer review
    path('register_farmer_review/', ReactView_Register_farmer_review.as_view(), name="anything"),# for pending businesmen payment register
    path('get_farmer_review/', ReactView_Search_farmer_review.as_view(), name="anything"),#for get pending businesmen payment   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


