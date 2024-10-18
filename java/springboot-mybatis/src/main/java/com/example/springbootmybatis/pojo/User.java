package com.example.springbootmybatis.pojo;

import java.util.Date;

public class User {
    private Integer id;
    private String username;
    private String password;
    private String nickname;
    private String email;
    private String phone;
    private String gender;
    private String bank_id;
    private String card_id;
    private String address;
    private String wx_id;
    private String avatar;
    private Date create_time;


    public User(Integer id, String username, String password, String nickname, String email, String phone, String gender, String bank_id, String card_id, String address, String wx_id, String avatar, Date create_time) {
        this.id = id;
        this.username = username;
        this.password = password;
        this.nickname = nickname;
        this.email = email;
        this.phone = phone;
        this.gender = gender;
        this.bank_id = bank_id;
        this.card_id = card_id;
        this.address = address;
        this.avatar = avatar;
        this.wx_id = wx_id;
        this.create_time = create_time;
    }

    public Integer getId() { return id; }
    public void setId() { this.id = id; }
    public  String getUsername() { return username; }
    public void setUsername() { this.username = username; }
}
