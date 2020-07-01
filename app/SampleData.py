import random

from paytmpg import LibraryConstants
from paytmpg import EnumCurrency, EChannelId, UserSubWalletType
from paytmpg import ExtendInfo, ShippingInfo, GoodsInfo, UserInfo, PaymentMode, Money


class SampleData:

    @staticmethod
    def get_channel_id():
        return EChannelId.WEB

    @staticmethod
    def get_shipping_info():
        shipping_info1 = ShippingInfo()
        shipping_info1.set_first_name("fname")
        shipping_info1.set_last_name("lname")
        shipping_info1.set_email("abc@xyz.com")
        shipping_info1.set_merchant_shipping_id("id1")
        shipping_info1.set_address1("Address 1")
        shipping_info1.set_address2("Address 2")
        shipping_info1.set_carrier("Carrier 1")
        """set charge amount as per your amount and then get money"""
        shipping_info1.set_charge_amount(SampleData.get_money())
        shipping_info1.set_city_name("Abc")
        shipping_info1.set_state_name("Xyz")
        shipping_info1.set_mobile_no("1234567890")
        shipping_info1.set_tracking_no("1122334455")

        shipping_info2 = ShippingInfo()
        shipping_info2.set_first_name("firstname")
        shipping_info2.set_last_name("lastname")
        shipping_info2.set_email("xyz@abc.com")
        shipping_info2.set_merchant_shipping_id("id2")
        shipping_info2.set_address1("Address line 1")
        shipping_info2.set_address2("Address line 2")
        shipping_info2.set_carrier("Carrier 2")
        """set charge amount as per your amount and then get money"""
        shipping_info2.set_charge_amount(SampleData.get_money())
        shipping_info2.set_city_name("xxx")
        shipping_info2.set_state_name("xxx")
        shipping_info2.set_mobile_no("7777777777")
        shipping_info2.set_tracking_no("xxxxxxxxxx")

        info = list()
        info.append(shipping_info1)
        info.append(shipping_info2)
        return info

    @staticmethod
    def get_goods_info():
        """This is list of GoodsInfo"""
        goods1 = GoodsInfo()
        goods1.set_merchant_goods_id("goods_id1")
        goods1.set_merchant_shipping_id("shipping_id1")
        goods1.set_snapshot_url("snapshot_url")
        goods1.set_description("desc")
        goods1.set_category("category")
        goods1.set_quantity("qty")
        goods1.set_unit("unit")
        goods1.set_price(SampleData.get_money())
        goods1.set_extend_info(SampleData.get_extend_info())
        goods2 = GoodsInfo()
        goods2.set_merchant_goods_id("goods_id2")
        goods2.set_merchant_shipping_id("shipping_id2")
        goods2.set_snapshot_url("url")
        goods2.set_description("description")
        goods2.set_category("category")
        goods2.set_quantity("str_type")
        goods2.set_unit("unit")
        goods2.set_price(SampleData.get_money())
        goods2.set_extend_info(SampleData.get_extend_info())
        goods = list()
        goods.append(goods1)
        goods.append(goods2)
        return goods

    @staticmethod
    def get_money():
        return Money(EnumCurrency.INR, "1.00")

    @staticmethod
    def get_disable_payment_modes():
        payment_mode1 = PaymentMode("CC")
        payment_mode1.channels = list()
        payment_mode1.channels.append(EChannelId.APP)
        payment_mode1.channels.append(EChannelId.WEB)

        payment_mode2 = PaymentMode("DC")
        payment_mode2.channels = list()
        payment_mode2.channels.append(EChannelId.APP)
        payment_mode2.channels.append(EChannelId.WEB)

        disable_mode = list()
        disable_mode.append(payment_mode1)
        disable_mode.append(payment_mode2)
        return disable_mode

    @staticmethod
    def get_enable_payment_modes():
        payment_mode1 = PaymentMode("CC")
        payment_mode1.channels = list()
        payment_mode1.channels.append(EChannelId.APP)
        payment_mode1.channels.append(EChannelId.WEB)

        payment_mode2 = PaymentMode("DC")
        payment_mode2.channels = list()
        payment_mode2.channels.append(EChannelId.APP)
        payment_mode2.channels.append(EChannelId.WEB)

        enable_mode = list()
        enable_mode.append(payment_mode1)
        enable_mode.append(payment_mode2)
        return enable_mode

    @staticmethod
    def get_extend_info():
        extend_info = ExtendInfo()
        extend_info.set_udf1("udf1")
        extend_info.set_udf2("udf2")
        extend_info.set_udf3("udf3")
        extend_info.set_merc_unq_ref("mercUnqRef")
        extend_info.set_comments("comment")
        extend_info.set_amount_to_be_refunded("1")
        sub_wallet_amount = dict()
        sub_wallet_amount[LibraryConstants.Request.FOOD_WALLET] = "2"
        sub_wallet_amount[LibraryConstants.Request.GIFT_WALLET] = "2.5"
        extend_info.set_sub_wallet_amount(sub_wallet_amount)
        return extend_info

    @staticmethod
    def get_user_info():
        user_info = UserInfo()
        user_info.set_cust_id("cid")
        user_info.set_address("address str")
        user_info.set_email("abc@xyz.com")
        user_info.set_first_name("JOHN")
        user_info.set_last_name("MILLER")
        user_info.set_mobile("1234567890")
        user_info.set_pincode("123123")
        return user_info

    @staticmethod
    def get_paytm_sso_token():
        return None # "Paytm sso token str type"

    @staticmethod
    def get_work_flow():
        return None # "str type"

    @staticmethod
    def get_promo_code():
        return None # "str type"

    @staticmethod
    def get_emi_option():
        return None # "str type"

    @staticmethod
    def get_card_token_required():
        return None # "str type"

    @staticmethod
    def get_cart_validation_required():
        return None # "str type"

    @staticmethod
    def get_sub_wallet_amount():
        """
        :return: dict(UserSubWalletType, BigDecimal) Object for the required Refund
        """
        sub_wallet_amount = dict()
        sub_wallet_amount[UserSubWalletType.FOOD] = "1.00"
        sub_wallet_amount[UserSubWalletType.GIFT] = "1.00"
        return sub_wallet_amount

    @staticmethod
    def get_extra_params_map():
        """
        extraParamsMap.put("purpose", "merchant purpose");
        extraParamsMap.put("data", "merchant data");
        :return: Map(String, Object) Object for the required
        """
        extra_params_map = dict()
        extra_params_map["data"] = "data"
        extra_params_map["purpose"] = "merchant purpose"
        return extra_params_map

    ALPHA_NUMERIC_STRING = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    @classmethod
    def generate_random_string(cls, length):
        random_string = []
        while length != 0:
            index = random.randint(0, len(cls.ALPHA_NUMERIC_STRING)-1)
            random_string.append(cls.ALPHA_NUMERIC_STRING[index])
            length -= 1
        return ''.join(random_string)
