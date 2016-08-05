 SELECT 
			 *
			FROM offer o
			where year(o.offer_valid_to) - year(o.offer_valid_from) < 100 
			and available_cnt >= 0
			and sellings_price >= 0 
			and valid_offer_flag >= 0 
			and breakfast_included_flag >= 0 
			limit 1000
