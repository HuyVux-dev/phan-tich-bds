import time
import csv
import undetected_chromedriver as uc

def main():
    # Tạo trình duyệt headless
    browser = uc.Chrome(headless=False, use_subprocess=False)

    # Tạo file để lưu trạng thái
    f = open("status.csv", mode='w', encoding='utf-8')
    f.close()

    start_page = 2
    end_page = 20  # Số trang sẽ crawl
    location = "nha-dat-ban-ha-noi"
    base_url = f"https://batdongsan.com.vn/{location}/p"

    quantity = 0

    for page in range (start_page, end_page+1):
        page_url = base_url + str(page)
        print(f"Start crawling page {page_url}")
        try:
            browser.get(page_url)
            # Sleep to load page content
            time.sleep(3)
            # Lướt xuống cuối trang
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            all_posts = browser.find_elements("xpath", "//a[@class='js__product-link-for-product-id']")
            links = []
            for post in all_posts:
                links.append(post.get_attribute('href'))
            for link in links:
                print("Crawling ", link)
                try:
                    browser.get(link)
                    html_name = link.split('/')[-1]
                    html_source = browser.page_source
                    with open(f"data/{html_name}.html", "w", encoding='utf-8') as file:
                        # Lưu source page
                        file.write(html_source)
                    print("Done")
                except:
                    print("Error Post")
                    continue

            with open('status.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # Ghi thêm dòng mới vào file
                new_row = [page_url, len(all_posts), quantity]
                writer.writerow(new_row)
            print("Số bài viết mới: ", len(links))
            print("Tổng số bài viết: ", quantity)
        except:
            print("ERORR PAGE")
            continue
        print("#" * 100)
        
    browser.close()

if __name__ == "__main__":
    main()
