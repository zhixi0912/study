package com.example.springbootmybatis.mapper;
import com.example.springbootmybatis.pojo.User;
import org.apache.ibatis.annotations.Mapper;
@Mapper
public interface UserMapper {
    @Select("select * from sys_user where id = #(id)")
    public User findById(Integer id);
}
