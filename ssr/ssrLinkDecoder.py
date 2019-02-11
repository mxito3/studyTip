import base64


def parse():
   while True:
       ssr = input('请输入需要解析的ssr链接:').strip()

       if ssr == 'q' or ssr == 'quit':
           break

       if ssr.startswith('ss://'):
           base64_encode_str = ssr[5:]
           parse_ss(base64_encode_str)
           continue

       if ssr.startswith('ssr://'):
           base64_encode_str = ssr[6:]
           parse_ssr(base64_encode_str)


def parse_ss(base64_encode_str):
   decode_str = base64_decode(base64_encode_str)
   parts = decode_str.split(':')
   if len(parts) != 3:
       print('不能解析SS链接: %s' % base64_encode_str)
       return
   method = parts[0]
   password_and_ip = parts[1]
   port = parts[2]

   pass_and_server = password_and_ip.split('@')
   password = pass_and_server[0]
   server = pass_and_server[1]
   print("解析结果:")
   print('加密方法: %s, 密码: %s, server: %s, port: %s' % (method, password, server, port))


def parse_ssr(base64_encode_str):
   decode_str = base64_decode(base64_encode_str)
   parts = decode_str.split(':')
   if len(parts) != 6:
       print('不能解析SSR链接: %s' % base64_encode_str)
       return

   server = parts[0]
   port = parts[1]
   protocol = parts[2]
   method = parts[3]
   obfs = parts[4]
   password_and_params = parts[5]

   password_and_params = password_and_params.split("/?")

   password_encode_str = password_and_params[0]
   password = base64_decode(password_encode_str)
   params = password_and_params[1]

   param_parts = params.split('&')

   param_dic = {}
   for part in param_parts:
       key_and_value = part.split('=')
       param_dic[key_and_value[0]] = key_and_value[1]

   obfsparam = base64_decode(param_dic['obfsparam'])
   protoparam = base64_decode(param_dic['obfsparam'])
   remarks = base64_decode(param_dic['remarks'])
   group = base64_decode(param_dic['group'])

   print("解析结果:")

   print('server: %s, port: %s, 协议: %s, 加密方法: %s, 密码: %s, 混淆: %s, 混淆参数: %s, 协议参数: %s, 备注: %s, 分组: %s'
         % (server, port, protocol, method, password, obfs, obfsparam, protoparam, remarks, group))


def fill_padding(base64_encode_str):

   need_padding = len(base64_encode_str) % 4 != 0

   if need_padding:
       missing_padding = 4 - need_padding
       base64_encode_str += '=' * missing_padding
   return base64_encode_str


def base64_decode(base64_encode_str):
   base64_encode_str = fill_padding(base64_encode_str)
   return base64.urlsafe_b64decode(base64_encode_str).decode('utf-8')


if __name__ == '__main__':
   parse()