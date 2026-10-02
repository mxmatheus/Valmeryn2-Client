SERVER_NAME			= "Valmeryn2"
SERVER_IP			= "127.0.0.1"
CH1_NAME			= "CH1"
CH2_NAME			= "CH2"
PORT_1				= 24011
PORT_2				= 24021
PORT_AUTH			= 24000
PORT_MARK			= 24011

STATE_NONE = "..."

STATE_DICT = {
	0 : "....",
	1 : "NORM",
	2 : "BUSY",
	3 : "FULL"
}

SERVER01_CHANNEL_DICT = {
	1:{"key":11,"name":CH1_NAME,"ip":SERVER_IP,"tcp_port":PORT_1,"udp_port":PORT_1,"state":STATE_NONE,},
	2:{"key":12,"name":CH2_NAME,"ip":SERVER_IP,"tcp_port":PORT_2,"udp_port":PORT_2,"state":STATE_NONE,},
}

REGION_NAME_DICT = {
	0 : "",		
}

REGION_AUTH_SERVER_DICT = {
	0 : {
		1 : { "ip":SERVER_IP, "port":PORT_AUTH, },

	}		
}

REGION_DICT = {
	0 : {
		1 : { "name" :SERVER_NAME, "channel" : SERVER01_CHANNEL_DICT, },						
	},
}

MARKADDR_DICT = {
	10 : { "ip" : SERVER_IP, "tcp_port" : PORT_MARK, "mark" : "10.tga", "symbol_path" : "10", },
}
